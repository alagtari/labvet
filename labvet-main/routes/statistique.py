from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
import crud.statistique as statistique
from database import  SessionLocal

router = APIRouter(tags=['statistique'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.get('/statistique')
def get_demandes(db: Session = Depends(get_db) ):
    return statistique.statistiques(db)

