
from sqlalchemy.orm import Session
import models, schemas

def get_methode(db: Session, id: int):
    return db.query(models.Methode).filter(models.Methode.id == id).first()

def get_all_methodes(db: Session):
    return db.query(models.Methode).all()

def get_methodes_by_designation(db: Session,designation:str):
    return db.query(models.Methode).filter(models.Methode.designation == designation).first()

def delete_methode(db: Session, id: int):
    methode =db.query(models.Methode).filter(models.Methode.id == id).first()
    db.delete(methode)
    db.commit()
    return True

def create_methode(db: Session, methode: schemas.methode):
    m = models.Methode(id= methode.id,designation=methode.designation)
    db.add(m)
    db.commit()
    return True

def update_methode(db: Session,methode: schemas.methode):
    db_methode = get_methode(db,methode.id)
    db_methode.designation = methode.designation
    db.commit()
    return True



    
 