
import hashlib
import time
from sqlalchemy.orm import Session
import models, schemas
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
    db_user = models.User(name=user['name'], email=user['email'],password=mdp,cin=user['cin'],tel=user['tel'],photo=str.encode(user['photo']),role=user['role'],contrat=str.encode(user['contrat']),datecr=round(time.time() * 1000))
    db.add(db_user)
    db.commit()
   
    



def update_user(user: schemas.UserBaseMini ,db :Session):
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    send_email = False
    if db_user.password != user.password or db_user.email != user.email  :
       send_email =True 
    db_user.name = user.name
    db_user.tel = user.tel
    db_user.role  = user.role
    db_user.email= user.email
    db_user.cin= user.cin
    if(db_user.password !=user.password):
        password = hashlib.md5(user.password.encode())
        db_user.password=password.hexdigest()
    db.commit()
    return send_email

    
