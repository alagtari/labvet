from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.demande as demande, app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal


router = APIRouter(tags=['demande'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/demandes/all")
def get_demandes( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        demandes = demande.get_demandes(db)
        return {"status" :  200 , "data" : demandes }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/demandes/create")
async def create_demande(d:schemas.Demande ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_demande = demande.get_demande_by_ref(db,d.ref)
        if db_demande:
          return {"status" : 400 , "message" : "demande already exists"}
        returned_id = demande.create_demande(db,d)
        return   {"status" : 200 , "message": "demande created." , "id":returned_id}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    




@router.get("/demandes/byid")
def get_demande_by_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)): 
        db_demande= demande.get_demande_by_ref(db,id)
        if not db_demande:
            return {"status" : 404 , "message" : "demande not found"}    
        return {"status" :  200 , "data" : db_demande }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/demandes/getClientBydemande")
def get_client_by_demande_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)): 
        db_demande= demande.get_demande_by_ref(db,id)
        if not db_demande:
            return {"status" : 404 , "message" : "demande not found"}    
        return {"status" :  200 , "data" : db_demande.client}
    else:
        return{"status" : 401 ,"message":"token expired"}



@router.get("/demandes/getEchantillonsByDemande")
def get_echantillons_by_demande_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)): 
        db_demande = demande.get_demande_by_ref(db,id)
        if not db_demande:
            return {"status" : 404 , "message" : "demande not found"}    
        return {"status" :  200 , "data" : db_demande.echantillons }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.delete("/demandes/delete")
def delete_demande(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):  
        if not demande.get_demande_by_ref(db,id):
              return {"status" : 404 , "message" : "demande not found"} 
        demande.delete_demande(db,id)
        return {"status" :  200 , "message" : "demande deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}

@router.put("/demandes/update")
def update_demande(e: schemas.Demande,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        if not demande.get_demande_by_ref(db,e.ref) :
            return {"status" : 404 , "message" : "echantillon not found"}    
        demande.update_demande(db,e)
        return {"status" : 200 , "message":"echantillon updated"} 
    else:
        return {"status": 401 , "message" : "Token expired!"}
    

