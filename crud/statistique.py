from sqlalchemy.orm import Session
import models,schemas

def statistiques(db: Session):
    stat = {}
    stat['client'] = len(db.query(models.Client).all())
    stat['demande'] = len(db.query(models.Demande).all())
    stat['echantillon_totale'] = len(db.query(models.Echantillon).all())
    stat['demande_traire'] = len(db.query(models.Demande).filter(models.Demande.etat == 'traire').all())
    stat['demande_en_cours'] = len(db.query(models.Demande).filter(models.Demande.etat == 'en cours').all())
    stat['methode'] = len(db.query(models.Methode).all())
    stat['parametre'] = len(db.query(models.Parametre).all())
    stat['nature'] = len(db.query(models.Nature).all())
    stat['famille'] = len(db.query(models.Famille).all())
    return stat

