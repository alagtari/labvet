from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.users as users,app.crud.parametre as parametre,app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal


router = APIRouter(tags=['parametre'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/parametres/all")
def get_parametres( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        parametres = parametre.get_parametres(db)
        return {"status" :  200 , "data" : parametres }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/parametres/create")
async def create_parametre(param:schemas.parametre ,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        accessed_user = users.get_user_by_email(db, email=email)
        if accessed_user.role != 'Admin' :
          return{"status" : 403,"message" :"Not Authorized"} 
        db_parametre = parametre.get_parametre_by_id(db,param.id)
        if db_parametre:
          return {"status" : 400 , "message" : "parametre already exists"}
        returned_id = parametre.create_parametre(db,param)
        return   {"status" : 200 , "message": "parametre created." , "id" : returned_id}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    




@router.get("/parametres/byid")
def get_parametre_by_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        param = parametre.get_parametre_by_id(db,id)
        if not param :
            return {"status" : 404 , "message" : "parametre not found"}    
        return {"status" :  200 , "data" : param }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/parametres/getNatureByParametre")
def get_natures_by_parametre_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        param = parametre.get_parametre_by_id(db,id)
        if not param:
            return {"status" : 404 , "message" : "parametre not found"}    
        return {"status" :  200 , "data" : param.natures }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/parametres/getMethodeByParametre")
def get_methodes_by_parametre_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        param = parametre.get_parametre_by_id(db,id)
        if not param:
            return {"status" : 404 , "message" : "parametre not found"}    
        return {"status" :  200 , "data" : param.methodes }
    else:
        return{"status" : 401 ,"message":"token expired"}
    
@router.get("/parametres/getEchantillonByParametre")
def get_echantillons_by_parametre_id(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        param = parametre.get_parametre_by_id(db,id)
        if not param:
            return {"status" : 404 , "message" : "parametre not found"}    
        return {"status" :  200 , "data" : param.echantillons }
    else:
        return{"status" : 401 ,"message":"token expired"}


@router.delete("/parametres/delete")
def delete_parametre(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        if db_user.role != 'Admin' :
          return {"status" : 403 , "message" : "Unauthorized"}  
        if not parametre.get_parametre_by_id(db,id):
              return {"status" : 404 , "message" : "parametre not found"} 
        parametre.delete_parametre(db,id)
        return {"status" :  200 , "message" : "parametre deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    

