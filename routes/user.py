import hashlib
from fastapi import Depends,  HTTPException,APIRouter,Request
from sqlalchemy.orm import Session
import crud.users as users, schemas ,tokens
from database import  SessionLocal
from mailsender import SendMail

router = APIRouter(tags=['users'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



ADMIN_EMAIL_ADDRESS = ''
ADMIN_EMAIL_PASSWORD = ''

#lawem ma yrajaach pwd
@router.get("/users/all")
def read_users( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'admin' :
          raise HTTPException(status_code=403, detail="not authorized")  
        returned_users = users.get_users(db)
        return returned_users 
    else:
        return{"token expired"}
    



@router.post("/users/create")
def create_user(user: schemas.UserCreate,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        accessed_user = users.get_user_by_email(db, email=email)
        if accessed_user.role != 'admin' :
          raise HTTPException(status_code=403, detail="not authorized")  
        
        db_user = users.get_user_by_email(db, email=user.email)
        if db_user:
          raise HTTPException(status_code=400, detail="Email already registered") 
        mail = SendMail(ADMIN_EMAIL_ADDRESS,ADMIN_EMAIL_PASSWORD,user.email,user.password,user.name)
        mail.send() 
        user.password = hashlib.md5(user.password.encode())
        return users.create_user(db=db, user=user)  
    else:
        return{"token expired"}
    
    



@router.put("/users/update")
def update_user(user: schemas.UserBaseMini,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'admin' :
          raise HTTPException(status_code=403, detail="not authorized")  
        return users.update_user(user=user) 
    else:
        return{"token expired"}



@router.delete("/users/delete")
def delete_user(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'admin' :
          raise HTTPException(status_code=403, detail="not authorized")  
        return users.delete_user(db=db, id=id)
    else:
        return{"token expired"}
    



@router.get('/users/info')
def get_info(request : Request , db: Session  = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        return {db_user}
    else:
        return{"token expired"}