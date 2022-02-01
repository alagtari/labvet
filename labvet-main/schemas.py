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



class UserBase(UserBaseMini):
    email: str
    cin : str
    contrat :str
    id:int
    name : str
    phoyo : str
    role : str
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



class methode(BaseModel):
    id: int
    designation : str

class source(BaseModel):
    id: int
    designation : str

class nature(BaseModel):
    id: int
    designation : str    
