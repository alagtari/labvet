
import time
from sqlalchemy.orm import Session
import models, schemas
import mysql.connector
import datetime

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    users = db.query(models.User).all()
    list_of_users =list()
    
    for user in users :
        if (user.role !="Admin"):
            u = {}
            
            u['name'] = user.name
            u['tel'] = user.tel
            u['photo'] = user.photo
            u['role']  = user.role
            u['email'] = user.email
            u['cin'] = user.cin
            u['contrat'] = user.contrat
            u['id'] = user.id
            u['datecr'] = datetime.datetime.utcfromtimestamp(float(user.datecr) // 1000).strftime('%Y-%m-%d %H:%M:%S')

            list_of_users.append(u)
    return list_of_users    


def delete_user(db: Session, id: int):
    db_user =db.query(models.User).filter(models.User.id == id).first()
    with open("results.txt" , "w") as f:
        f.write(str(db_user))
    db.delete(db_user)
    db.commit()

def create_user(db: Session, user,mdp):
    db_user = models.User(name=user['name'], email=user['email'],password=mdp,cin=user['cin'],tel=user['tel'],photo=user['photo'],role=user['role'],contrat=user['contrat'],datecr=round(time.time() * 1000))
    db.add(db_user)
    db.commit()
   
    

def update_user(user: schemas.UserBaseMini):
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "labvet")
    cursor = mydb.cursor()
    sql ="UPDATE utilisateur SET name = %s, tel = %s, photo = %s, role = %s , password = %s , cin = %  WHERE id = %s"
    val =  (user.name, user.tel, user.photo , user.role , user.password ,user.cin,user.id)
    cursor.execute(sql,val)
    mydb.commit()
    return {'status': 200}



    
