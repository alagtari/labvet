
from sqlalchemy.orm import Session
import models, schemas
import mysql.connector

def get_methode(db: Session, id: int):
    return db.query(models.Methode).filter(models.Methode.id == id).first()

def get_all_methodes(db: Session):
    return db.query(models.Methode).all()

def get_methodes_by_designation(db: Session,designation:str):
    return db.query(models.Methode).filter(models.Methode.designation == designation).first()

def delete_methode(db: Session, id: int):
    methode =db.query(models.Methode).filter(models.Methode.id == id).first()
    db.delete(methode)
    db.commit()
    return {'status': 'Success'}

def create_methode(db: Session, methode: schemas.methode):
    methode = models.Methode(id= methode.id,designation=methode.designation)
    db.add(methode)
    db.commit()
    return {'status': 'Success'}

def update_client(methode: schemas.methode):
    mydb = mysql.connector.connect(host = "localhost" , client = "root" , password = "" , database = "labvet")
    cursor = mydb.cursor()
    sql ="UPDATE methode SET designation = %s WHERE id = %s"
    val =  (methode.designation,methode.id)
    cursor.execute(sql,val)
    mydb.commit()
    return {'status': 'Success'}



    
