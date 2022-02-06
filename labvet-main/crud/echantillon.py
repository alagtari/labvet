
from sqlalchemy.orm import Session
import models, schemas ,crud.nature as nature 
from barcode import EAN13 
from barcode.writer import ImageWriter 
import base64

def get_echantillon_by_ref_codebarre(db: Session, ref_codebarre:str):
    return db.query(models.Echantillon).filter(models.Echantillon.refCodebarre == ref_codebarre).first()


def get_echantillons(db: Session):
    db_ech  = db.query(models.Echantillon).all()
    for ech in db_ech :
        ech.barcode = base64.b64decode(ech.barcode)
    return db_ech   

def delete_echantillon(db: Session, ref_codebarre:str):
    db_echantillon =db.query(models.Echantillon).filter(models.Echantillon.refCodebarre == ref_codebarre).first()
    db.delete(db_echantillon)
    db.commit()
    return True

def create_echantillon(db: Session, echantillon: schemas.echantillon ):
    n = nature.get_nature(db,echantillon.idn)
    ref_codebarre = '000000'+str(echantillon.idd)+echantillon.ref + str(echantillon.idn)+str(n.famille_id)+str(echantillon.idp)
    db_echantillon = models.Echantillon(refCodebarre= ref_codebarre,id= echantillon.id,ref= echantillon.ref ,quantite=echantillon.quantite,nlot=echantillon.nlot,temperature=echantillon.temperature)
    db.add(db_echantillon)
    db.commit()

    my_code = EAN13(ref_codebarre, writer=ImageWriter()) 
    my_code.save("code_a_barre")

    echan =  db.query(models.Echantillon).filter(models.Echantillon.refCodebarre == ref_codebarre).first()
    ref_codebarre = ref_codebarre + str(db_echantillon.id)
    echan.refCodebarre = ref_codebarre 
    with open('code_a_barre.png', 'rb') as f :
        barcode = f.read()
    echan.barcode = barcode
    db.commit()
    st = models.parametre_echantillon.insert().values(parametre_id= echantillon.idp , echantillon_refCodebarre=ref_codebarre)
    st2 = models.nature_echantillon.insert().values(nature_id= echantillon.idn , echantillon_refCodebarre=ref_codebarre)
    st3 = models.demande_echantillon.insert().values(demande_ref= echantillon.idd , echantillon_refCodebarre=ref_codebarre)

    
    
    db.execute(st)
    db.commit()
    db.execute(st2)
    db.commit()
    db.execute(st3)
    db.commit()

    return True

def update_echantillon(db: Session,echantillon: schemas.echantillonUpdate):
    db_echantillon = get_echantillon_by_ref_codebarre(db, echantillon.ref_codebarre)
    db_echantillon.quantite = echantillon.quantite
    db_echantillon.nlot  = echantillon.nlot
    db_echantillon.temperature = echantillon.temperature
    db_echantillon.ref = echantillon.ref
    db.commit()
    return True

