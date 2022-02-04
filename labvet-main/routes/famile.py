from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import crud.users as users,crud.famille as famille, schemas ,tokens
from database import  SessionLocal


router = APIRouter(tags=['famille'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/familles/all")
def get_familles( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        familles = famille.get_familles(db)
        return {"status" :  200 , "data" : familles }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/familles/create")
async def create_famille(f:schemas.famille ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        accessed_user = users.get_user_by_email(db, email=email)
        if accessed_user.role != 'Admin' :
          return{"status" : 403,"message" :"Not Authorized"} 
        db_famille = famille.get_famille_by_id(db,f.idf)
        if db_famille:
          return {"status" : 400 , "message" : "famille already exists"}
        famille.create_famille(db,f)
        return   {"status" : 200 , "message": "famille created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    



@router.put("/familles/update")
def update_famille(f: schemas.famille,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status": 403 , "message" : "Unauthorized"}
        if not famille.get_famille_by_id(db,f.idf):
           return {"status" : 404 , "message":"famille not found"} 
        famille.update_famille(db,f)                       
        return {"status" : 200 , "message":"famille updated"} 
    else:
        return {"status": 401 , "message" : "Token expired!"}

@router.get("/familles/byid")
def get_famille_by_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"} 
        if db_user.role != 'Admin' :
              return {"status" : 403 , "message" : "Unauthorized"} 
        f = famille.get_famille_by_id(db,id)
        if not f :
            return {"status" : 404 , "message" : "famille not found"}    
        return {"status" :  200 , "data" : f }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/familles/getNaturesByFamId")
def get_natures_by_famille_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"} 
        if db_user.role != 'Admin' :
              return {"status" : 403 , "message" : "Unauthorized"} 
        f = famille.get_famille_by_id(db,id)
        if not f :
            return {"status" : 404 , "message" : "famille not found"}    
        return {"status" :  200 , "data" : f.natures }
    else:
        return{"status" : 401 ,"message":"token expired"}
    

@router.delete("/familles/delete")
def delete_famille(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"}  
        if not famille.get_famille_by_id(db,id) :
            return {"status" : 404 , "message" : "famille not found"}   
        famille.delete_famille(db,id)
        return {"status" :  200 , "message" : "famille deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    

