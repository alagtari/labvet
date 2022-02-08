from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import crud.users as users,crud.methode as methode, schemas ,tokens
from database import  SessionLocal


router = APIRouter(tags=['methode'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/methodes/all")
def get_methodes( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        methodes = methode.get_all_methodes(db)
        return {"status" :  200 , "data" : methodes }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/methodes/create")
async def create_methode(meth:schemas.methode ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        accessed_user = users.get_user_by_email(db, email=email)
        if accessed_user.role != 'Admin' :
          return{"status" : 403,"message" :"Not Authorized"} 
        db_methode = methode.get_methode(db,meth.id)
        if db_methode:
          return {"status" : 400 , "message" : "methode already exists"}
        methode.create_methode(db,meth)
        return   {"status" : 200 , "message": "methode created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    



@router.get("/methodes/byid")
def get_methode_by_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        meth = methode.get_methode(db,id)
        if not meth :
            return {"status" : 404 , "message" : "methode not found"}    
        return {"status" :  200 , "data" : meth }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/methodes/getParametresByMthode")
def get_Parametres_by_methode_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        m = methode.get_methode(db,id)
        if not m:
            return {"status" : 404 , "message" : "methode not found"}    
        return {"status" :  200 , "data" : m.parametres }
    else:
        return{"status" : 401 ,"message":"token expired"}
    

@router.delete("/methodes/delete")
def delete_methode(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"}  
        if not methode.get_methode(db,id) :
            return {"status" : 404 , "message" : "methode not found"}   
        methode.delete_methode(db,id)
        return {"status" :  200 , "message" : "methode deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    

