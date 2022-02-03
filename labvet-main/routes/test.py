from fastapi import Depends,APIRouter
from sqlalchemy import null
from sqlalchemy.orm import Session
import crud.client as client, schemas ,tokens
from database import  SessionLocal

router = APIRouter(tags=['test'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.get('/get_demandes')
def get_demandes(id :int, db: Session = Depends(get_db) ):
    return client.get_demandes_by_cient(db , id)

@router.post('/add')
def get_demandes(c:schemas.Client , db: Session = Depends(get_db) ):
    return client.create_client(db,c)
                