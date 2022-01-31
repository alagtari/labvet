from sqlalchemy import Column, Integer, String ,DATE
from database import Base

class User(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    password = Column(String(8))
    name = Column(String(40))
    cin = Column(String(8))
    tel = Column(String(8))
    photo = Column(String(200))
    contrat = Column(String(200))
    role = Column(String(20))
    datecr = Column(DATE)

class Client(Base):
    __tablename__ = "client"

    idc = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    raisonSocial = Column(String(8))
    responsable = Column(String(40))
    adresse = Column(String(8))
    tel = Column(String(8))
 
