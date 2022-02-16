
from sqlalchemy.orm import Session
import models, schemas

def get_famille_by_id(db: Session, idf: str):
    return db.query(models.Famille).filter(models.Famille.idf == idf).first()


def get_familles(db: Session):
    faimlles = db.query(models.Famille).all()
    res = []
    for faimlle in faimlles:
        fam ={}
        fam['idf'] = faimlle.idf
        fam['nomf'] = faimlle.nomf
        fam['nature_id'] = faimlle.nature_id
        fam['nature'] = faimlle.nature.designation
        res.append(fam)
    return res  
    
def delete_famille(db: Session, idf: str):
    db_famille =db.query(models.Famille).filter(models.Famille.idf == idf).first()
    db.delete(db_famille)
    db.commit()
    return True

def create_famille(db: Session, famille: schemas.famille):
    db_famille = models.Famille(nomf=famille.nomf,nature_id=famille.idn)
    db.add(db_famille)
    db.flush()
    db.refresh(db_famille)
    db.commit()
    return db_famille.idf

def update_famille(db: Session,famille: schemas.famille):
    db_famille = get_famille_by_id(db, famille.idf)
    db_famille.nomf = famille.nomf
    db.commit()
    return True

def get_natures_by_famille(db: Session,idf :str) :
    famille = get_famille_by_id(db, idf)
    return famille.nature


    
