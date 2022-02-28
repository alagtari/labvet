
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas


def get_client_by_id(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.idc == client_id).first()


def get_clients_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()


def get_clients(db: Session):
    clients = db.query(models.Client).all()
    for c in clients :
        d = c.demandes
    return clients    

def delete_client(db: Session, idc: int):
    db_client =db.query(models.Client).filter(models.Client.idc == idc).first()
    db.delete(db_client)
    db.commit()
    return True

def create_client(db: Session, client: schemas.Client):
    db_client = models.Client(idc= client.idc ,email=client.email,tel=client.tel,raisonSocial=client.raisonSocial,adresse=client.adresse,responsable=client.responsable)
    db.add(db_client)
    db.commit()
    return True

def update_client(db: Session,client: schemas.Client):
    db_client = get_client_by_id(db, client.idc)
    db_client.email = client.email
    db_client.tel = client.tel
    db_client.raisonSocial  = client.raisonSocial
    db_client.adresse = client.adresse
    db_client.responsable  = client.responsable
    db.commit()
    return True

def get_demandes_by_cient(db: Session,client_id :int) :
    client = get_client_by_id(db, client_id)
    return client.demandes



    
