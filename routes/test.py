from fastapi import Depends,APIRouter
from sqlalchemy import null
from sqlalchemy.orm import Session
import crud.parametre as parametre, schemas ,tokens
from database import  SessionLocal

router = APIRouter(tags=['test'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.get('/get')
def get_demandes(id :int, db: Session = Depends(get_db) ):
    return parametre.get_parametre_by_id(db,id).methodes

