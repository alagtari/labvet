from typing import List
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
    ref :int
    observation :str
    date_reception = int
    preleveur :str
    controle :str
    client_id :int
    etat :str


class methode(BaseModel):
    id: int
    designation : str

class Departement(BaseModel):
    id: int
    nom : str    

class nature(BaseModel):
    id: int
    designation : str  
    

class parametre(BaseModel):
    id: int
    nomp : str
    id_dep :List[int]

class famille(BaseModel):
    idf  :  int
    nomf :  str
    idn  :  int 


class echantillonUpdate(BaseModel):
    id :int
    ref :str
    quantite :int
    nlot :int 
    temperature :str
    ref_codebarre:str
    designation :str



class echantillon(BaseModel):
    id:int
    id_dep :List[int]
    quantite :int
    nlot :int 
    temperature :str
    idn:int
    idp:List[int]
    idd:int
    idf:int
    designation :str


class Client(BaseModel):
    idc :int
    email:str
    raisonSocial :str
    responsable :str
    adresse :str
    tel :str

