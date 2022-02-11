from sqlalchemy import  LargeBinary, Column, Integer, String , ForeignKey,Table,BigInteger,LargeBinary
from sqlalchemy.orm import relationship,backref
from database import Base


class User(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    password = Column(String(200))
    name = Column(String(40))
    cin = Column(String(8))
    tel = Column(String(8))
    photo = Column(LargeBinary(length=(2**32)-1))
    contrat = Column(LargeBinary(length=(2**32)-1))
    role = Column(String(20))
    datecr = Column(BigInteger)


class Client(Base):
    __tablename__ = "client"

    idc = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    raisonSocial = Column(String(8))
    responsable = Column(String(40))
    adresse = Column(String(8))
    tel = Column(String(8))
    demandes = relationship("Demande", back_populates="client")
    
parametre_nature = Table('Parametre_nature', Base.metadata,
    Column('parametre_id', ForeignKey('parametre.id')),
    Column('nature_id', ForeignKey('nature.id'))
) 

parametre_methode = Table('Parametre_methode', Base.metadata,
    Column('parametre_id', ForeignKey('parametre.id')),
    Column('methode_id', ForeignKey('methode.id'))
) 

parametre_echantillon = Table('Parametre_echantillon', Base.metadata,
    Column('parametre_id', ForeignKey('parametre.id')),
    Column('echantillon_id', ForeignKey('echantillon.id'))
) 

class Demande(Base):
    __tablename__ = "demande"

    ref = Column(Integer, primary_key=True, index=True)
    observation = Column(String(40), unique=True, index=True)
    date_reception = Column(BigInteger)
    preleveur = Column(String(100))
    controle = Column(String(100))
    etat = Column(String(100))
    codeDemande = Column(String(20))
    client_id = Column(Integer, ForeignKey('client.idc'))
    client = relationship("Client", back_populates="demandes")
    echantillons = relationship("Echantillon", back_populates="demande")





class Parametre(Base):
    __tablename__ = "parametre"

    id = Column(Integer, primary_key=True, index=True)
    nomp = Column(String(40))
    echantillons = relationship("Echantillon", secondary=parametre_echantillon)
    methodes = relationship("Methode",secondary=parametre_methode)
    natures = relationship("Nature",secondary=parametre_nature)

class Methode(Base):
    __tablename__ = "methode"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))
    parametres = relationship("Parametre",secondary=parametre_methode)




class Nature(Base):
    __tablename__ = "nature"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))
    familles = relationship("Famille", back_populates="nature")
    parametres = relationship("Parametre",secondary=parametre_nature)
    echantillons = relationship("Echantillon", back_populates="nature")


class Famille(Base):
    __tablename__ = "famille"

    idf = Column(Integer, primary_key=True, index=True)
    nomf = Column(String(40))
    nature_id = Column(Integer, ForeignKey('nature.id'))
    nature = relationship(Nature, backref=backref("famille" , cascade="all,delete"))
    
class Echantillon(Base):
    __tablename__ = "echantillon"
    id = Column(Integer, primary_key=True, index=True)
    barcode = Column(String(13))
    ref = Column(String(4))
    dep = Column(String(2))
    quantite = Column(Integer)
    nlot = Column(Integer)
    temperature = Column(String(20)) 
    datecr = Column(BigInteger)
    idd = Column(Integer, ForeignKey('demande.ref'))
    idn = Column(Integer, ForeignKey('nature.id'))
    demande = relationship("Demande", back_populates="echantillons")
    parametres = relationship("Parametre", secondary=parametre_echantillon)
    nature = relationship("Nature", back_populates="echantillons")
    
