from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import crud.users as users,crud.echantillon as echantillon,crud.nature as nature,crud.parametre as parametre, schemas ,tokens
from database import  SessionLocal


router = APIRouter(tags=['echantillon'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()



#matekhdemch mayhebch ydecodi UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
@router.get("/echantillons/all")
def get_echantillons( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        echantillons = echantillon.get_echantillons(db)
        return {"status" :  200 , "data" : echantillons }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    


#tekhdem
@router.post("/echantillons/create")
async def create_echantillon(ech:schemas.echantillon ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_ref_codebarre(db,ech.ref_codebarre)
        if db_echantillon:
          return {"status" : 400 , "message" : "echantillon already exists"} 
        echantillon.create_echantillon(db,ech)
        return   {"status" : 200 , "message": "echantillon created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    



#matekhdemch mayhebch ydecodi UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
@router.get("/echantillons/byrefCodebarre")
def get_echantillon_by_refCodebarre(refCodebarre :str ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_ref_codebarre(db,refCodebarre)
        if not db_echantillon :
            return {"status" : 404 , "message" : "echantillon not found"}    
        return {"status" :  200 , "data" : db_echantillon.barcode }
    else:
        return{"status" : 401 ,"message":"token expired"}

#tekhdem
@router.get("/echantillons/getDemandeByEchantillon")
def get_Demande_by_echantillon(refCodebarre :str ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_ref_codebarre(db,refCodebarre)
        if not db_echantillon :
            return {"status" : 404 , "message" : "echantillon not found"}    
        return {"status" :  200 , "data" : db_echantillon.demandes }
    else:
        return{"status" : 401 ,"message":"token expired"}

#tekhdem
@router.get("/echantillons/getNaturesByEchantillon")
def get_natures_by_echantillon(refCodebarre :str ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_ref_codebarre(db,refCodebarre)
        if not db_echantillon :
            return {"status" : 404 , "message" : "echantillon not found"}    
        return {"status" :  200 , "data" : db_echantillon.natures }
    else:
        return{"status" : 401 ,"message":"token expired"}


#tekhdem
@router.get("/echantillons/getParametresByEchantillon")
def get_Parametres_by_echantillon(refCodebarre :str ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_echantillon = echantillon.get_echantillon_by_ref_codebarre(db,refCodebarre)
        if not db_echantillon :
            return {"status" : 404 , "message" : "echantillon not found"}    
        return {"status" :  200 , "data" : db_echantillon.parametres }
    else:
        return{"status" : 401 ,"message":"token expired"}

#tekhdem
@router.delete("/echantillons/delete")
def delete_echantillon(refcodebarre :str ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        if not echantillon.get_echantillon_by_ref_codebarre(db,refcodebarre) :
            return {"status" : 404 , "message" : "echantillon not found"}   
        echantillon.delete_echantillon(db,refcodebarre)
        return {"status" :  200 , "message" : "echantillon deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    
#tekhdem
@router.put("/echantillons/update")
def update_echantillon(e: schemas.echantillonUpdate,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        if not echantillon.get_echantillon_by_ref_codebarre(db,e.ref_codebarre) :
            return {"status" : 404 , "message" : "echantillon not found"}    
        echantillon.update_echantillon(db,e)
        return {"status" : 200 , "message":"echantillon updated"} 
    else:
        return {"status": 401 , "message" : "Token expired!"}
