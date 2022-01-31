from fastapi import Depends, FastAPI, HTTPException , Request
from sqlalchemy.orm import Session
import crud.user as user, models, schemas ,tokens
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from mailsender import SendMail

models.Base.metadata.create_all(bind=engine)
db = Session()
origins = ["*"]
middleware = [ Middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])]
app = FastAPI(middleware=middleware)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ADMIN_EMAIL_ADDRESS = ''
ADMIN_EMAIL_PASSWORD = ''


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/login')
def login( db: Session = Depends(get_db),request:schemas.Login = Depends()):
    db_user = user.get_user_by_email(db, email=request.username)
    if not db_user:
        raise HTTPException(status_code=404, detail="no such table account with this email address")
    elif request.password != db_user.password:
        raise  HTTPException(status_code=403, detail="wrong password")
    access_token = tokens.create_access_token(request.username)
    return {"access_token": access_token, "token_type": "bearer"}

#lawem ma yrajaach pwd
@app.get("/users/all")
def read_users( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = user.get_user_by_email(db, email=email)
        if db_user.role != 'admin' :
          raise HTTPException(status_code=403, detail="not authorized")  
        users = user.get_users(db)
        return users 
    else:
        return{"token expired"}
    



@app.post("/users/create")
def create_user(user: schemas.UserCreate,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        accessed_user = user.get_user_by_email(db, email=email)
        if accessed_user.role != 'admin' :
          raise HTTPException(status_code=403, detail="not authorized")  
        
        db_user = user.get_user_by_email(db, email=user.email)
        if db_user:
          raise HTTPException(status_code=400, detail="Email already registered") 
        mail = SendMail(ADMIN_EMAIL_ADDRESS,ADMIN_EMAIL_PASSWORD,user.email,user.password,user.name)
        mail.send() 
        return user.create_user(db=db, user=user)  
    else:
        return{"token expired"}
    
    



@app.put("/users/update")
def update_user(user: schemas.UserBaseMini,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = user.get_user_by_email(db, email=email)
        if db_user.role != 'admin' :
          raise HTTPException(status_code=403, detail="not authorized")  
        return user.update_user(user=user) 
    else:
        return{"token expired"}



@app.delete("/users/delete")
def delete_user(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = user.get_user_by_email(db, email=email)
        if db_user.role != 'admin' :
          raise HTTPException(status_code=403, detail="not authorized")  
        return user.delete_user(db=db, id=id)
    else:
        return{"token expired"}
    



@app.get('/users/info')
def get_info(request : Request , db: Session  = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = user.get_user_by_email(db, email=email)
        return {db_user}
    else:
        return{"token expired"}