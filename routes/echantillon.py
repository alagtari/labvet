from cmath import nan
from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import crud.demande as demande,crud.echantillon as echantillon,crud.nature as nature,crud.parametre as parametre, schemas ,tokens,models
from database import  SessionLocal


router = APIRouter(tags=['echantillon'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()



@router.get("/echantillons/all")
def get_echantillons( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        echantillons = echantillon.get_echantillons(db)
        return {"status" :  200 , "data" : echantillons }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/echantillons/create")
async def create_echantillon(ech:schemas.echantillon ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        if not nature.get_nature(db,ech.idn) :
            return   {"status" : 404 , "message" : "nature not found."}  
        if not demande.get_demande_by_ref(db,ech.idd) :
            return   {"status" : 404 , "message" : "demande not found."}      
        echantillon.create_echantillon(db,ech)
        return   {"status" : 200 , "message": "echantillon created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    



@router.get("/echantillons/byid")
def get_echantillon_by_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_id(db,id)
        if not db_echantillon :
            return {"status" : 404 , "message" : "echantillon not found"}    
        return {"status" :  200 , "data" : db_echantillon }
    else:
        return{"status" : 401 ,"message":"token expired"}


@router.get("/echantillons/getDemandeByEchantillon")
def get_Demande_by_echantillon(id:int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_id(db,id)
        if not db_echantillon :
            return {"status" : 404 , "message" : "echantillon not found"}    
        return {"status" :  200 , "data" : db_echantillon.demande }
    else:
        return{"status" : 401 ,"message":"token expired"}


@router.get("/echantillons/getNaturesByEchantillon")
def get_natures_by_echantillon(id:int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_id(db,id)
        if not db_echantillon :
            return {"status" : 404 , "message" : "echantillon not found"}    
        return {"status" :  200 , "data" : db_echantillon.nature }
    else:
        return{"status" : 401 ,"message":"token expired"}



@router.get("/echantillons/getParametreByEchantillon")
def get_Parametre_by_echantillon(id:int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_id(db,id)
        if not db_echantillon :
            return {"status" : 404 , "message" : "echantillon not found"}    
        return {"status" :  200 , "data" : db_echantillon.parametre }
    else:
        return{"status" : 401 ,"message":"token expired"}


@router.delete("/echantillons/delete")
def delete_echantillon(id:int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        if not echantillon.get_echantillon_by_id(db,id) :
            return {"status" : 404 , "message" : "echantillon not found"}   
        echantillon.delete_echantillon(db,id)
        return {"status" :  200 , "message" : "echantillon deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    

@router.put("/echantillons/update")
def update_echantillon(e: schemas.echantillonUpdate,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        if not echantillon.get_echantillon_by_id(db,e.id) :
            return {"status" : 404 , "message" : "echantillon not found"}    
        echantillon.update_echantillon(db,e)
        return {"status" : 200 , "message":"echantillon updated"} 
    else:
        return {"status": 401 , "message" : "Token expired!"}
