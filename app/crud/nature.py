
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas


def get_nature(db: Session, id: int):
    return db.query(models.Nature).filter(models.Nature.id == id).first()

def get_all_natures(db: Session):
    natures  =  db.query(models.Nature).all()
    for nature in natures:
        n  = nature.parametres
        f = nature.familles
    return natures

def get_natures_by_designation(db: Session,designation:str):
    return db.query(models.Nature).filter(models.Nature.designation == designation).first()

def delete_nature(db: Session, id: int):
    nature =db.query(models.Nature).filter(models.Nature.id == id).first()
    db.delete(nature)
    db.commit()
    return True

def create_nature(db: Session, nature: schemas.nature):
    nature = models.Nature(designation=nature.designation)
    db.add(nature)
    db.flush()
    db.refresh(nature)
    db.commit()
    return nature.id

def update_nature(db:Session ,nature: schemas.nature):
    db_nature = get_nature(db,nature.id)
    db_nature.designation = nature.designation
    db.commit()
    return True



    
