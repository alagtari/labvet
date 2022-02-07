
from sqlalchemy.orm import Session
import models, schemas ,crud.nature as nature 
from barcode import EAN13 
from barcode.writer import ImageWriter 
import base64
import time
def get_echantillon_by_id(db: Session, id:str):
    return db.query(models.Echantillon).filter(models.Echantillon.id == id).first()


def get_echantillons(db: Session):
    db_ech  = db.query(models.Echantillon).all()
    return db_ech   

def delete_echantillon(db: Session, id:int):
    db_echantillon =db.query(models.Echantillon).filter(models.Echantillon.id == id).first()
    db.delete(db_echantillon)
    db.commit()
    return True

def create_echantillon(db: Session, echantillon: schemas.echantillon ):
    n = nature.get_nature(db,echantillon.idn)
    datecr = round(time.time() * 1000)
    db_echantillon = models.Echantillon(id= echantillon.id,idn= echantillon.idn,idp= echantillon.idp,idd= echantillon.idd,ref= echantillon.ref ,quantite=echantillon.quantite,nlot=echantillon.nlot,temperature=echantillon.temperature,datecr=datecr)
    db.add(db_echantillon)
    db.commit()
    db_echantillon =db.query(models.Echantillon).filter(models.Echantillon.datecr == datecr).first()
    ref_codebarre = str(db_echantillon.idd)+'00000'+db_echantillon.ref+str(db_echantillon.idn)+str(n.famille_id)+str(db_echantillon.idp)+str(db_echantillon.id)
    print(ref_codebarre)
    my_code = EAN13(ref_codebarre, writer=ImageWriter()) 
    my_code.save("code_a_barre")
    with open('code_a_barre.png', 'rb') as f :
        barcode = base64.b64encode(f.read())
    db_echantillon.barcode = barcode
    
    db.commit()
    return True


def update_echantillon(db: Session,echantillon: schemas.echantillonUpdate):
    db_echantillon = get_echantillon_by_id(db, echantillon.id)
    db_echantillon.quantite = echantillon.quantite
    db_echantillon.nlot  = echantillon.nlot
    db_echantillon.temperature = echantillon.temperature
    db.commit()
    return True

