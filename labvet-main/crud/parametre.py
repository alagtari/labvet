
from sqlalchemy.orm import Session
import models, schemas

def get_parametre_by_id(db: Session, id: str):
    return db.query(models.Parametre).filter(models.Parametre.id == id).first()


def get_parametres(db: Session):
    return db.query(models.Parametre).all()

def delete_parametre(db: Session, id: str):
    db_parametre =db.query(models.Parametre).filter(models.Parametre.id == id).first()
    db.delete(db_parametre)
    db.commit()
    return True

def create_parametre(db: Session, parametre: schemas.parametre):
    db_parametre = models.Parametre(id= parametre.id ,nomp=parametre.nomp)
    db.add(db_parametre)
    db.commit()
    return True

def update_parametre(db: Session,parametre: schemas.parametre):
    db_parametre = get_parametre_by_id(db, parametre.id)
    db_parametre.nomp = parametre.nomp
    db.commit()
    return True


    
