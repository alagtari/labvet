
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas
import mysql.connector

def get_source(db: Session, id: int):
    return db.query(models.Source).filter(models.Source.id == id).first()

def get_all_sources(db: Session):
    return db.query(models.Source).all()

def get_sources_by_designation(db: Session,designation:str):
    return db.query(models.Source).filter(models.Source.designation == designation).first()

def delete_source(db: Session, id: int):
    source =db.query(models.Source).filter(models.Source.id == id).first()
    db.delete(source)
    db.commit()
    return {'status': 200}

def create_source(db: Session, source: schemas.source):
    source = models.Source(id= source.id,designation=source.designation)
    db.add(source)
    db.commit()
    return {'status': 200}

def update_client(source: schemas.source):
    mydb = mysql.connector.connect(host = "localhost" , client = "root" , password = "" , database = "labvet")
    cursor = mydb.cursor()
    sql ="UPDATE source SET designation = %s WHERE id = %s"
    val =  (source.designation,source.id)
    cursor.execute(sql,val)
    mydb.commit()
    return {'status': 200}



    
