
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas
 
import barcode as BARCODE
from barcode.writer import ImageWriter 
import base64
import time
def get_echantillon_by_id(db: Session, id:str):
    echantillon = db.query(models.Echantillon).filter(models.Echantillon.id == id).first()
    ech = {}
    ech['echantillon'] = echantillon
    echantillon.departements
    echantillon.parametres
    echantillon.nature
    
    


    Code39 = BARCODE.get_barcode_class('code39')
    code39 = Code39(echantillon.barcode, add_checksum=False, writer=ImageWriter())
    code39.save('code_a_barre')

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
       echantillon.departements
       echantillon.demande
       echantillon.parametres
       echantillon.nature

       Code39 = BARCODE.get_barcode_class('code39')
       code39 = Code39(echantillon.barcode, add_checksum=False, writer=ImageWriter())
       code39.save('code_a_barre')
       
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
    db_echantillon = models.Echantillon(idn= echantillon.idn,idd= echantillon.idd,designation= echantillon.designation ,quantite=echantillon.quantite,nlot=echantillon.nlot,temperature=echantillon.temperature,datecr=datecr)
    db.add(db_echantillon)
    db.flush()
    db.refresh(db_echantillon)
    db.commit()
    for id in echantillon.idp :
        association = models.parametre_echantillon.insert().values(parametre_id=id , echantillon_id=db_echantillon.id)
        db.execute(association)
        db.commit()
    for id in echantillon.id_dep :
        association = models.departement_echantillon.insert().values(departement_id=id , echantillon_id=db_echantillon.id)
        db.execute(association)
        db.commit()    
    
    db_echantillon.barcode = str(echantillon.idd)+str(echantillon.idn)+str(echantillon.idf)+str(db_echantillon.id)

    db.commit()
    return True


def update_echantillon(db: Session,echantillon: schemas.echantillonUpdate):
    db_echantillon = db.query(models.Echantillon).filter(models.Echantillon.id == echantillon.id).first()
    db_echantillon.quantite = echantillon.quantite
    db_echantillon.nlot = echantillon.nlot
    db_echantillon.temperature = echantillon.temperature
    db_echantillon.designation = echantillon.designation
    
    db.commit()
    return True

