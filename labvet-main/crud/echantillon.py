
from sqlalchemy.orm import Session
import models, schemas

def get_echantillon_by_ref(db: Session, ref: str):
    return db.query(models.Echantillon).filter(models.Echantillon.ref == ref).first()


def get_echantillons(db: Session):
    return db.query(models.Echantillon).all()

def delete_echantillon(db: Session, ref: str):
    db_echantillon =db.query(models.Echantillon).filter(models.Echantillon.ref == ref).first()
    db.delete(db_echantillon)
    db.commit()
    return True

def create_echantillon(db: Session, echantillon: schemas.echantillon):
    db_echantillon = models.Echantillon(ref= echantillon.ref ,barcode=echantillon.barcode,quantite=echantillon.quantite,nlot=echantillon.nlot,temperature=echantillon.temperature)
    db.add(db_echantillon)
    db.commit()
    return True

def update_echantillon(db: Session,echantillon: schemas.echantillon):
    db_echantillon = get_echantillon_by_ref(db, echantillon.ref)
    db_echantillon.barcode = echantillon.barcode
    db_echantillon.quantite = echantillon.quantite
    db_echantillon.nlot  = echantillon.nlot
    db_echantillon.temperature = echantillon.temperature
    db.commit()
    return True

def get_demandes_by_echantillon(db: Session,ref :str) :
    echantillon = get_echantillon_by_ref(db, ref)
    return echantillon.demande


def get_parametres_by_echantillon(db: Session,ref :str) :
    echantillon = get_echantillon_by_ref(db, ref)
    return echantillon.parametres


    
