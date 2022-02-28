from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.client as client, app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal

router = APIRouter(tags=['users'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@router.get("/client/all")
def read_client( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        returned_client = client.get_clients(db)
        return {"status" : 200,"data" :returned_client }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/clients/create")
async def create_client(c:schemas.Client ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_client = client.get_client_by_id(db,c.idc)
        if db_client:
          return {"status" : 400 , "message" : "client already exists"}
        client.create_client(db,c)
        return   {"status" : 200 , "message": "client created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    
    



@router.put("/clients/update")
def update_client(c: schemas.Client,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        client.update_client(db,c)
        return {"status" : 200 , "message":"client updated"} 
    else:
        return {"status": 401 , "message" : "Token expired!"}

@router.get("/clients/byid")
def get_client_by_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_client = client.get_client_by_id(db,id)
        if not db_client:
              return {"status" : 404 , "message" : "client not found"} 
        return {"status" :  200 , "data" : db_client }
    else:
        return{"status" : 401 ,"message":"token expired"}
    


@router.delete("/clients/delete")
def delete_client(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):  
        if not client.get_client_by_id(db,id):
              return {"status" : 404 , "message" : "client not found"} 
        client.delete_client(db,id)
        return {"status" :  200 , "message" : "client deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/clients/getDemandesByClient")
def get_demandes_by_client(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_client = client.get_client_by_id(db,id)
        if not db_client:
            return {"status" : 404 , "message" : "client not found"}    
        return {"status" :  200 , "data" : db_client.demandes }
    else:
        return{"status" : 401 ,"message":"token expired"}
    