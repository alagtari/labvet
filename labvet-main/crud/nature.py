
from sqlalchemy.orm import Session
import models, schemas
import mysql.connector

def get_nature(db: Session, id: int):
    return db.query(models.Nature).filter(models.Nature.id == id).first()

def get_all_natures(db: Session):
    return db.query(models.Nature).all()

def get_natures_by_designation(db: Session,designation:str):
    return db.query(models.Nature).filter(models.Nature.designation == designation).first()

def delete_nature(db: Session, id: int):
    nature =db.query(models.Nature).filter(models.Nature.id == id).first()
    db.delete(nature)
    db.commit()
    return {'status': 200}

def create_nature(db: Session, nature: schemas.nature):
    nature = models.Nature(id= nature.id,designation=nature.designation)
    db.add(nature)
    db.commit()
    return {'status': 200}

def update_client(nature: schemas.nature):
    mydb = mysql.connector.connect(host = "localhost" , client = "root" , password = "" , database = "labvet")
    cursor = mydb.cursor()
    sql ="UPDATE nature SET designation = %s WHERE id = %s"
    val =  (nature.designation,nature.id)
    cursor.execute(sql,val)
    mydb.commit()
    return {'status': 200}



    
