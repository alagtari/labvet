from sqlalchemy import Column, Integer, String ,DATE,BLOB
from database import Base

class User(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    password = Column(String(8))
    name = Column(String(40))
    cin = Column(String(8))
    tel = Column(String(8))
    photo = Column(BLOB)
    contrat = Column(BLOB)
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
 
class Methode(Base):
    __tablename__ = "methode"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))

class Nature(Base):
    __tablename__ = "nature"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))

 
class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))

 
