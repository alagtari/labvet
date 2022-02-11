from fastapi import Depends,APIRouter
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
def login( request:schemas.Login ,db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, email=request.username)
    if not db_user:
       return {'status' :404  , 'message' : "Adresse Email incorrecte." }
    elif request.password != db_user.password:
          return {'status' :404  , 'message' : "Mot de passe incorrect." }
    access_token = tokens.create_access_token(request.username)
    return {"access_token": access_token, "token_type": "bearer" , "status" : 200 , "role" : db_user.role , "id" : db_user.id}
        