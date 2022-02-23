from sqlalchemy.orm import Session
import models, schemas

def get_parametre_by_id(db: Session, id: str):
    return db.query(models.Parametre).filter(models.Parametre.id == id).first()

def get_parametres(db: Session):
    parametres =  db.query(models.Parametre).all()
    for parametre in parametres:
        o1 = parametre.nature
        o2= parametre.methodes
    return parametres

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
    for id in parametre.id_dep :
        association = models.departement_parametre.insert().values(departement_id=id , parametre_id=db_parametre.id)
        db.execute(association)
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