from cgi import test
from fastapi import FastAPI
import  models
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from database import  engine
from  routes import auth,user,test as t

models.Base.metadata.create_all(bind=engine)

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

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(t.router)
