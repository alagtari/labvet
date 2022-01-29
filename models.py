from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    password = Column(String(30))
    name = Column(String(40))
    cin = Column(String(8))
    telephone = Column(String(8))
    photo = Column(String(200))
    role = Column(String(20))
