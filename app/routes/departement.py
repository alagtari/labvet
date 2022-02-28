from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.departement as departement,app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal


router = APIRouter(tags=['departement'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/departements/all")
def get_departements( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        departements = departement.get_all_departements(db)
        return {"status" :  200 , "data" : departements }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/departements/create")
async def create_departement(dep:schemas.Departement ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_departement = departement.get_departement(db,dep.id)
        if db_departement:
          return {"status" : 400 , "message" : "departement already exists"}
        departement.create_departement(db,dep)
        return   {"status" : 200 , "message": "departement created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    

@router.get("/departements/byid")
def get_departement_by_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        dep = departement.get_departement(db,id)
        if not dep :
            return {"status" : 404 , "message" : "departement not found"}    
        return {"status" :  200 , "data" : dep }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
    
@router.delete("/departements/delete")
def delete_departement(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)): 
        if not departement.get_departement(db,id) :
            return {"status" : 404 , "message" : "departement not found"}   
        departement.delete_departement(db,id)
        return {"status" :  200 , "message" : "departement deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    

