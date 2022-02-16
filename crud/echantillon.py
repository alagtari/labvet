
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
        barcode = "data:image/png;base64,"+str(base64.b64encode(f.read())).replace("b'" , "").replace("'" , "")
    ech['code_a_barre'] = barcode
    return ech


def get_echantillons(db: Session):
    db_echantillons  = db.query(models.Echantillon).all()
    echantillons = []
    for echantillon in db_echantillons :
       ech = {}
       ech['echantillon'] = echantillon
       p = echantillon.nature
       my_code = EAN13(echantillon.barcode, writer=ImageWriter()) 
       my_code.save("code_a_barre")
       with open('code_a_barre.png', 'rb') as f :
                barcode = base64.b64encode(f.read())
       ech['code a barre'] = barcode
       echantillons.append(ech)
    return ech   

def delete_echantillon(db: Session, id:int):
    db_echantillon =db.query(models.Echantillon).filter(models.Echantillon.id == id).first()
    db.delete(db_echantillon)
    db.commit()
    return True 

def create_echantillon(db: Session, echantillon: schemas.echantillon ):
    datecr = round(time.time() * 1000)
    if echantillon.ref == 'MIC':
        dep = '01'
    elif echantillon.ref == 'Phys':  
        dep = '02'   
    else :
        dep = '03'
<<<<<<< HEAD
    
    barcode = str(echantillon.idd)+'00000'+dep+str(echantillon.idf)+str(echantillon.idn)+str(echantillon.idp)
=======

    barcode = str(echantillon.idd)+'000000'+dep+str(echantillon.idf)+str(echantillon.idn)
>>>>>>> c2af95dd0f7c29880ce0979748e77aec49a217b1
    db_echantillon = models.Echantillon(dep = dep,barcode= barcode,idn= echantillon.idf,idd= echantillon.idd,ref= echantillon.ref ,quantite=echantillon.quantite,nlot=echantillon.nlot,temperature=echantillon.temperature,datecr=datecr)
    db.add(db_echantillon)
    db.flush()
    db.refresh(db_echantillon)
    db.commit()
    for id in echantillon.idp :
        association = models.parametre_echantillon.insert().values(parametre_id=id , echantillon_id=db_echantillon.id)
        db.execute(association)
        db.commit()
    db_echantillon.barcode = str(db_echantillon.id)+db_echantillon.barcode
    db.commit()
    return True


def update_echantillon(db: Session,echantillon: schemas.echantillonUpdate):
    db_echantillon = db.query(models.Echantillon).filter(models.Echantillon.id == echantillon.id).first()
    db_echantillon.quantite = echantillon.quantite
    db_echantillon.nlot = echantillon.nlot
    db_echantillon.temperature = echantillon.temperature
    
    db.commit()
    return True

