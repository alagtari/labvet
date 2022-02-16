from sqlalchemy.orm import Session
import models, schemas 
import time
import datetime
import crud.echantillon as echantillon
def get_demande_by_ref(db: Session, ref: int):
    return db.query(models.Demande).filter(models.Demande.ref == ref).first()


def get_demandes(db: Session):
    demandes =  db.query(models.Demande).all()
    res = []
    for demande in demandes:
        o = {}
        o['ref'] = demande.ref
        o['client'] = demande.client.email
        o['date_reception'] =datetime.datetime.utcfromtimestamp(float(demande.date_reception) // 1000).strftime('%Y-%m-%d %H:%M:%S')
        o['controle'] = demande.controle
        o['etat'] = demande.etat
        for ech in demande.echantillons:
            ech.nature
        o['echantillons'] = []
        for ech in demande.echantillons:
            ech = echantillon.get_echantillon_by_id(db , ech.id)
            o['echantillons'].append(ech)
        o['nbr'] = len(demande.echantillons)
        res.append(o)
    return res

def delete_demande(db: Session, ref: int):
    db_demande =db.query(models.Demande).filter(models.Demande.ref == ref).first()
    db.delete(db_demande)
    db.commit()
    return True

def create_demande(db: Session, demande: schemas.Demande):
    db_demande = models.Demande(etat='en cours',observation=demande.observation,date_reception=demande.date_reception,preleveur=demande.preleveur,controle=demande.controle,client_id=demande.client_id)
    db.add(db_demande)
    db.flush()
    db.refresh(db_demande)
    db.commit()
    db_demande.codeDemande = str(db_demande.ref)+str(round(time.time() * 1000))
    db.commit()

    return db_demande.ref

def update_demande(db: Session,demande: schemas.Demande):
    db_demande = get_demande_by_ref(db, demande.ref)
    db_demande.observation = demande.observation
    db_demande.date_reception = demande.date_reception
    db_demande.preleveur  = demande.preleveur
    db_demande.controle = demande.controle
    db_demande.client_id  = demande.client_id
    db_demande.etat = demande.etat
    db.commit()
    return True

def get_client_by_demande(db: Session,ref :int) :
    demande = get_demande_by_ref(db, ref)
    return demande.client


def get_echantillons_by_demande(db: Session,ref :int) :
    demande = get_demande_by_ref(db, ref)
    return demande.echantillons




    
