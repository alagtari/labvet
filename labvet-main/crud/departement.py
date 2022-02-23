
from sqlalchemy.orm import Session
import models, schemas

def get_departement(db: Session, id: int):
    return db.query(models.Departement).filter(models.Departement.id == id).first()

def get_all_departements(db: Session):
    deps =  db.query(models.Departement).all()
    for dep in deps:
        p = dep.parametres
    return deps

def delete_departement(db: Session, id: int):
    departement =db.query(models.Departement).filter(models.Departement.id == id).first()
    db.delete(departement)
    db.commit()
    return True

def create_departement(db: Session, departement: schemas.Departement):
    m = models.Departement(id= departement.id,nomdep=departement.nom)
    db.add(m)
    db.commit()
    return True




    
 