
from datetime import datetime
from sqlalchemy.orm import Session
import models, schemas
import mysql.connector

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    users = db.query(models.User).all()
    list_of_users =list()
    for user in users :
        u = schemas.UserBase(
            id = user.id,
            name= user.name,
            tel= user.tel, 
            photo = user.photo,
            role= user.role,
            email= user.email,
            cin = user.cin,
            contrat= user.contrat
        )
        list_of_users.append(u)
    return list_of_users    


def delete_user(db: Session, id: int):
    db_user =db.query(models.User).filter(models.User.id == id).first()
    db.delete(db_user)
    db.commit()
    return {'status': 200}

def create_user(db: Session, user: schemas.UserBase,mdp):
    db_user = models.User(id= user.id ,name=user.name, email=user.email,password=mdp,cin=user.cin,tel=user.tel,photo=user.photo,role=user.role,contrat=user.contrat,datecr=datetime.timestamp())
    db.add(db_user)
    db.commit()
    return {'status': 200}

def update_user(user: schemas.UserBaseMini):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "labvet")
    cursor = mydb.cursor()
    sql ="UPDATE utilisateur SET name = %s, tel = %s, photo = %s, role = %s  WHERE id = %s"
    val =  (user.name, user.tel, user.photo , user.role ,user.id)
    cursor.execute(sql,val)
    mydb.commit()
    return {'status': 200}



    
