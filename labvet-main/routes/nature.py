from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import crud.users as users,crud.nature as nature, schemas ,tokens
from database import  SessionLocal


router = APIRouter(tags=['nature'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/natures/all")
def get_natures( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        natures = nature.get_all_natures(db)
        return {"status" :  200 , "data" : natures }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/natures/create")
async def create_nature(n:schemas.nature ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        accessed_user = users.get_user_by_email(db, email=email)
        if accessed_user.role != 'Admin' :
          return{"status" : 403,"message" :"Not Authorized"} 
        db_nature = nature.get_nature(db,n.id)
        if db_nature:
          return {"status" : 400 , "message" : "nature already exists"}
        nature.create_nature(db,n)
        return   {"status" : 200 , "message": "nature created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    



@router.put("/natures/update")
def update_nature(n: schemas.nature,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status": 403 , "message" : "Unauthorized"}
        if not nature.get_nature(db,n.id):
           return {"status" : 404 , "message":"nature not found"} 
        nature.update_nature(db,n)                       
        return {"status" : 200 , "message":"nature updated"} 
    else:
        return {"status": 401 , "message" : "Token expired!"}

@router.get("/natures/byid")
def get_nature_by_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"} 
        if db_user.role != 'Admin' :
              return {"status" : 403 , "message" : "Unauthorized"} 
        n = nature.get_nature(db,id)
        if not n :
            return {"status" : 404 , "message" : "nature not found"}    
        return {"status" :  200 , "data" : n }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/natures/getFamilleByNature")
def get_famille_by_nature_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"} 
        if db_user.role != 'Admin' :
              return {"status" : 403 , "message" : "Unauthorized"} 
        n = nature.get_nature(db,id)
        if not n:
            return {"status" : 404 , "message" : "nature not found"}    
        return {"status" :  200 , "data" : n.famille }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/natures/getParametresByNature")
def get_Parametres_by_nature_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"} 
        if db_user.role != 'Admin' :
              return {"status" : 403 , "message" : "Unauthorized"} 
        n = nature.get_nature(db,id)
        if not n:
            return {"status" : 404 , "message" : "nature not found"}    
        return {"status" :  200 , "data" : n.parametres }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.delete("/natures/delete")
def delete_nature(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"}  
        if not nature.get_nature(db,id):
              return {"status" : 404 , "message" : "nature not found"} 
        nature.delete_nature(db,id)
        return {"status" :  200 , "message" : "nature deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    

