from ast import Str
from datetime import date
from pydantic import BaseModel



class Login(BaseModel):
    username: str
    password: str

class UserBaseMini(BaseModel):
    id: int
    name: str
    tel: str 
    photo : str
    role: str
    cin: str
    email:str
    password : str



class UserBase(UserBaseMini):
    contrat : str



class User(UserBase):
    class Config:
        orm_mode = True

class Client(BaseModel):
    idc: int
    email: str
    tel: str 
    raisonSocial : str
    adresse: str
    responsable : str


class Demande(BaseModel):
    ref :str
    observation :str
    date_reception = int
    preleveur :str
    controle :str
    client_id :int


class methode(BaseModel):
    id: int
    designation : str

class source(BaseModel):
    id: int
    designation : str

class nature(BaseModel):
    id: int
    designation : str  
    famille_id :   

class parametre(BaseModel):
    id: int
    nomp : str

class famille(BaseModel):
    idf: int
    nomf : str

class echantillon(BaseModel):
    ref :str
    barcode :str
    quantite :int
    nlot :int 
    temperature :str
