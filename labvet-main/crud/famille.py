
from sqlalchemy.orm import Session
import models, schemas

def get_famille_by_id(db: Session, idf: str):
    return db.query(models.Famille).filter(models.Famille.idf == idf).first()


def get_familles(db: Session):
    return db.query(models.Famille).all()

def delete_famille(db: Session, idf: str):
    db_famille =db.query(models.Famille).filter(models.Famille.idf == idf).first()
    db.delete(db_famille)
    db.commit()
    return True

def create_famille(db: Session, famille: schemas.famille):
    db_famille = models.Famille(idf= famille.idf ,nomf=famille.nomf)
    db.add(db_famille)
    db.commit()
    return True

def update_famille(db: Session,famille: schemas.famille):
    db_famille = get_famille_by_id(db, famille.idf)
    db_famille.nomf = famille.nomf
    db.commit()
    return True

def get_natures_by_famille(db: Session,idf :str) :
    famille = get_famille_by_id(db, idf)
    return famille.natures


    
