
from sqlalchemy.orm import Session
import models, schemas 
from barcode import EAN13 
from barcode.writer import ImageWriter 
import base64
import time
def get_echantillon_by_id(db: Session, id:str):
    echantillon = db.query(models.Echantillon).filter(models.Echantillon.id == id).first()
    ech = {}
    ech['echantillon'] = echantillon
    my_code = EAN13(echantillon.barcode, writer=ImageWriter()) 
    my_code.save("code_a_barre")
    with open('code_a_barre.png', 'rb') as f :
        barcode = base64.b64encode(f.read())
    ech['code a barre'] = barcode
    return ech


def get_echantillons(db: Session):
    db_echantillons  = db.query(models.Echantillon).all()
    echantillons = []
    for echantillon in db_echantillons :
       ech = {}
       ech['echantillon'] = echantillon
       my_code = EAN13(echantillon.barcode, writer=ImageWriter()) 
       my_code.save("code_a_barre")
       with open('code_a_barre.png', 'rb') as f :
                barcode = base64.b64encode(f.read())
       ech['code a barre'] = barcode
       echantillons.append(ech)
    return echantillons   

def delete_echantillon(db: Session, id:int):
    db_echantillon =db.query(models.Echantillon).filter(models.Echantillon.id == id).first()
    db.delete(db_echantillon)
    db.commit()
    return True 

def create_echantillon(db: Session, echantillon: schemas.echantillon ):
    datecr = round(time.time() * 1000)
    barcode = str(echantillon.idd)+'00000'+echantillon.ref+str(echantillon.idf)+str(echantillon.idn)+str(echantillon.idp)
    db_echantillon = models.Echantillon(barcode= barcode,idn= echantillon.idf,idp= echantillon.idp,idd= echantillon.idd,ref= echantillon.ref ,quantite=echantillon.quantite,nlot=echantillon.nlot,temperature=echantillon.temperature,datecr=datecr)
    db.add(db_echantillon)
    db.flush()
    db.refresh(db_echantillon)
    db.commit()
    db_echantillon.barcode = str(db_echantillon.id)+db_echantillon.barcode
    db.commit()
    return True


def update_echantillon(db: Session,echantillon: schemas.echantillonUpdate):
    db_echantillon = get_echantillon_by_id(db, echantillon.id)
    db_echantillon.quantite = echantillon.quantite
    db_echantillon.nlot  = echantillon.nlot
    db_echantillon.temperature = echantillon.temperature
    db.commit()
    return True

