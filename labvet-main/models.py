from sqlalchemy import BLOB, TEXT, Column, Integer, String ,DATE, ForeignKey,Table,BigInteger
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    password = Column(String(200))
    name = Column(String(40))
    cin = Column(String(8))
    tel = Column(String(8))
    photo = Column(TEXT)
    contrat = Column(TEXT)
    role = Column(String(20))
    datecr = Column(BigInteger)




class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))





class Client(Base):
    __tablename__ = "client"

    idc = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    raisonSocial = Column(String(8))
    responsable = Column(String(40))
    adresse = Column(String(8))
    tel = Column(String(8))
    demandes = relationship("Demande", back_populates="client")

class Demande(Base):
    __tablename__ = "demande"

    ref = Column(String(20), primary_key=True, index=True)
    observation = Column(String(40), unique=True, index=True)
    date_reception = Column(DATE)
    preleveur = Column(String(100))
    controle = Column(String(100))
    client_id = Column(Integer, ForeignKey('client.idc'))
    client = relationship("Client", back_populates="demandes")
    echantillons = relationship("Echantillon")


class Echantillon(Base):
    __tablename__ = "echantillon"

    ref = Column(String(20), primary_key=True, index=True)
    barcode = Column(BLOB)
    quantite = Column(Integer)
    nlot = Column(Integer)
    temperature = Column(String(20)) 
    demande = relationship("Demande")
    parametres = relationship("Parametre")

class Parametre(Base):
    __tablename__ = "parametre"

    id = Column(Integer, primary_key=True, index=True)
    nomp = Column(String(40))
    echantillons = relationship("Echantillon")
    methodes = relationship("Methode")
    natures = relationship("Nature")

class Methode(Base):
    __tablename__ = "methode"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))
    parametres = relationship("Parametre")

class Famille(Base):
    __tablename__ = "famille"

    idf = Column(Integer, primary_key=True, index=True)
    nomf = Column(String(40))
    natures = relationship("Nature", back_populates="famille")


class Nature(Base):
    __tablename__ = "nature"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))
    famille_id = Column(Integer, ForeignKey('famille.idf'))
    famille = relationship("Famille", back_populates="natures")
    parametres = relationship("Parametre")

    
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
    Column('echantillon_ref', ForeignKey('echantillon.ref'))
) 

demande_echantillon = Table('demande_echantillon', Base.metadata,
    Column('demande_ref', ForeignKey('demande.ref')),
    Column('echantillon_ref', ForeignKey('echantillon.ref'))
)
try:
        Demande.echantillons = relationship("Echantillon",secondary=demande_echantillon)
        Echantillon.demande = relationship("Demande",secondary=demande_echantillon)
        Echantillon.parametres = relationship("Parametre",secondary=parametre_echantillon)
        Parametre.echantillons = relationship("Echantillon",secondary=parametre_echantillon)
        Parametre.methodes = relationship("Methode",secondary=parametre_methode)
        Parametre.natures = relationship("Nature",secondary=parametre_nature)
        Methode.parametres = relationship("Parametre",secondary=parametre_methode)
        Nature.parametres = relationship("Parametre",secondary=parametre_nature)
finally:
    print('')        