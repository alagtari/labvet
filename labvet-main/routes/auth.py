from fastapi import Depends,  HTTPException,APIRouter
from sqlalchemy.orm import Session
import crud.users as users, schemas ,tokens
from database import  SessionLocal

router = APIRouter(tags=['Authentication'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.post('/login')
def login( db: Session = Depends(get_db),request:schemas.Login = Depends()):
    db_user = users.get_user_by_email(db, email=request.username)
    if not db_user:
       return {'status' :404  , 'message' : "Adresse Email incorrecte." }
    elif request.password != db_user.password:
          return {'status' :404  , 'message' : "Mot de passe incorrect." }
    access_token = tokens.create_access_token(request.username)
    return {"access_token": access_token, "token_type": "bearer" , "status" : 200}
        