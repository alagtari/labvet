
from sqlalchemy.orm import Session
import models, schemas

def get_nature(db: Session, id: int):
    return db.query(models.Nature).filter(models.Nature.id == id).first()

def get_all_natures(db: Session):
    return db.query(models.Nature).all()

def get_natures_by_designation(db: Session,designation:str):
    return db.query(models.Nature).filter(models.Nature.designation == designation).first()

def delete_nature(db: Session, id: int):
    nature =db.query(models.Nature).filter(models.Nature.id == id).first()
    db.delete(nature)
    db.commit()
    return True

def create_nature(db: Session, nature: schemas.nature):
    nature = models.Nature(id= nature.id,designation=nature.designation,famille_id=nature.famille_id)
    db.add(nature)
    db.commit()
    return True

def update_nature(db:Session ,nature: schemas.nature):
    db_nature = get_nature(db,nature.id)
    db_nature.designation = nature.designation
    db_nature.famille_id = nature.famille_id
    db.commit()
    return True



    
