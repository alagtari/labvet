
from sqlalchemy.orm import Session
import models, schemas
import mysql.connector

def get_clients(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_clients_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()


def get_clientss(db: Session):
    return db.query(models.Client).all()

def delete_client(db: Session, idc: int):
    db_client =db.query(models.Client).filter(models.Client.idc == idc).first()
    db.delete(db_client)
    db.commit()
    return {'status': 'Success'}

def create_client(db: Session, client: schemas.Client):
    db_client = models.Client(idc= client.idc ,email=client.email,tel=client.tel,raisonSocial=client.raisonSocial,adresse=client.adresse,responsable=client.responsable)
    db.add(db_client)
    db.commit()
    return {'status': 'Success'}

def update_client(client: schemas.Client):
    mydb = mysql.connector.connect(host = "localhost" , client = "root" , password = "" , database = "labvet")
    cursor = mydb.cursor()
    sql ="UPDATE client SET responsable = %s, raisonSocial = %s, tel = %s, email = %s,adresse  = %s  WHERE idc = %s"
    val =  (client.responsable , client.raisonSocial, client.tel, client.email , client.adresse ,client.idc)
    cursor.execute(sql,val)
    mydb.commit()
    return {'status': 'Success'}



    
