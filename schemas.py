from pydantic import BaseModel



class Login(BaseModel):
    email: str
    password: str

class UserBaseMini(BaseModel):
    id: int
    name: str
    telephone: str 
    photo : str
    role: str


class UserBase(UserBaseMini):
    email: str
    cin : str
   


class UserCreate(UserBase):
    password: str


class User(UserBase):
    class Config:
        orm_mode = True




