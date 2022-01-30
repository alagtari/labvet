from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from mailsender import SendMail

models.Base.metadata.create_all(bind=engine)
db = Session()
app = FastAPI()

ADMIN_EMAIL_ADDRESS = ''
ADMIN_EMAIL_PASSWORD = ''



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/create")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    mail = SendMail(ADMIN_EMAIL_ADDRESS,ADMIN_EMAIL_PASSWORD,user.email,user.password,user.name)
    mail.send() 
    return crud.create_user(db=db, user=user)



@app.get("/users/all", response_model=List[schemas.User])
def read_users( db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.put("/users/update")
def update_user(user: schemas.UserBaseMini, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User dosen't exist ")
    return crud.update_user(user=user)
    
@app.delete("/users/delete")
def delete_user(id : int , db: Session = Depends(get_db)):
    db_user = crud.get_user(db,user_id=id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User dosen't exist")
    return crud.delete_user(db=db, id=id)




@app.post('/login')
def login(data : schemas.Login , db: Session = Depends(get_db)):

    username = data.username
    password = data.password
    
    db_user = crud.get_user_by_email(db, email=username)
    if not db_user:
        raise HTTPException(status_code=404, detail="no such table account with this email address")
    elif password != db_user.password:
        raise  HTTPException(status_code=403, detail="wrong password")
    return {'status': 'Success','role' :db_user.role}


