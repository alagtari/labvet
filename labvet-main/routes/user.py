import hashlib
from fastapi import Depends,  HTTPException,APIRouter,Request
from sqlalchemy.orm import Session
import crud.users as users, schemas ,tokens
from database import  SessionLocal
from mailsender import SendMail
import json

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
        if db_user.role != 'Admin' :
            return {"status" : 403 , "message" : "Not Authorized."}
        returned_users = users.get_users(db)
        return returned_users 
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/users/create")
async def create_user(request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    body = json.loads(await request.body())
    with open("result.txt" , "w") as file:
        file.write(str(body))
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        accessed_user = users.get_user_by_email(db, email=email)
        if accessed_user.role != 'Admin' :
          return{"status" : 403,"message" :"Not Authorized"} 
        
        db_user = users.get_user_by_email(db, email=body['email'])
        if db_user:
          return {"status" : 400 , "message" : "User already exists"}
        #mail = SendMail(ADMIN_EMAIL_ADDRESS,ADMIN_EMAIL_PASSWORD,body['email'],body['cin'],body['name'])
        #mail.send() 
        password = hashlib.md5(body['cin'].encode())
        users.create_user(db=db, user=body,mdp=password.hexdigest())
        return   {"status" : 200 , "message": "user created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    



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
    with open("result.txt" , "w") as file:
        file.write(token)
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        return {"status" : 200 , "data" : db_user}