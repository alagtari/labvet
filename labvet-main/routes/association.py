from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import crud.association as association,crud.parametre as parametre,crud.methode as methode,crud.nature as nature, schemas ,tokens
from database import  SessionLocal


router = APIRouter(tags=['association'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@router.post("/associations/createParametreMethode")
def create_association_parametre_methode(idp :int,idm :int,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        
        if not parametre.get_parametre_by_id(db,idp) :
            return   {"status" : 404 , "message" : "parametre not found."} 
        if not methode.get_methode(db,idm) :
            return   {"status" : 404 , "message" : "methode not found."}     
        if not association.create_association_parametre_methode(db,idp,idm):
          return   {"status" : 400 , "message" : "association already exists"} 
        return   {"status" : 200 , "message": "association created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    

@router.post("/associations/createParametreNature")
def create_association_parametre_nature(idp :int,idn :int,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
         
        if not parametre.get_parametre_by_id(db,idp) :
            return   {"status" : 404 , "message" : "parametre not found."} 
        if not nature.get_nature(db,idn) :
            return   {"status" : 404 , "message" : "nature not found."}
        if not association.create_association_parametre_nature(db,idp,idn) :
              return   {"status" : 400 , "message" : "association already exists"}
        return   {"status" : 200 , "message": "association created."}
    else:
        return{"status" : 403,"message" :"token expired"}
       