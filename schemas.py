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
    datecr :date
    contrat :str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    class Config:
        orm_mode = True




