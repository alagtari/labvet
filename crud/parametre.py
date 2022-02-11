from sqlalchemy.orm import Session
import models, schemas

def get_parametre_by_id(db: Session, id: str):
    return db.query(models.Parametre).filter(models.Parametre.id == id).first()


def get_parametres(db: Session):
    parametres =  db.query(models.Parametre).all()
    res = []
    for parametre in parametres:
        o = {}
        o['id'] = parametre.id
        o['nomp'] = parametre.nomp
        o['nature'] = parametre.natures[0].designation
        o['methodes'] = parametre.methodes
        res.append(o)
    return res

def delete_parametre(db: Session, id: str):
    db_parametre =db.query(models.Parametre).filter(models.Parametre.id == id).first()
    db.delete(db_parametre)
    db.commit()
    return True

def create_parametre(db: Session, parametre: schemas.parametre):
    db_parametre = models.Parametre(nomp=parametre.nomp)
    db.add(db_parametre)
    db.flush()
    db.refresh(db_parametre)
    db.commit()
    return db_parametre.id

def update_parametre(db: Session,parametre: schemas.parametre):
    db_parametre = get_parametre_by_id(db, parametre.id)
    db_parametre.nomp = parametre.nomp
    db.commit()
    return True

def get_echantillons_by_parametre(db: Session,id :str) :
    parametre = get_parametre_by_id(db, id)
    return parametre.echantillons

def get_natures_by_parametre(db: Session,id :str) :
    parametre = get_parametre_by_id(db, id)
    return parametre.natures

def get_methodes_by_parametre(db: Session,id :str) :
    parametre = get_parametre_by_id(db, id)
    return parametre.methodes