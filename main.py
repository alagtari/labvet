from cgi import test
from fastapi import FastAPI
import  models
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from database import  engine
from  routes import test as t, auth,user,famile,nature,methode,echantillon,client,demande,association,statistique,parametre




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
app.include_router(famile.router)
app.include_router(nature.router)
app.include_router(methode.router)
app.include_router(parametre.router)
app.include_router(echantillon.router)
app.include_router(client.router)
app.include_router(demande.router)
app.include_router(association.router)
app.include_router(statistique.router)