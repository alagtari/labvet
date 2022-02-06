from sqlalchemy import BLOB, LargeBinary, Column, Integer, String ,DATE, ForeignKey,Table,BigInteger,LargeBinary
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
    photo = Column(LargeBinary(length=(2**32)-1))
    contrat = Column(LargeBinary(length=(2**32)-1))
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
    Column('echantillon_refCodebarre', ForeignKey('echantillon.refCodebarre'))
) 

demande_echantillon = Table('demande_echantillon', Base.metadata,
    Column('demande_ref', ForeignKey('demande.ref')),
    Column('echantillon_refCodebarre', ForeignKey('echantillon.refCodebarre'))
)

nature_echantillon = Table('nature_echantillon', Base.metadata,
    Column('nature_id', ForeignKey('nature.id')),
    Column('echantillon_refCodebarre', ForeignKey('echantillon.refCodebarre'))
)    

class Demande(Base):
    __tablename__ = "demande"

    ref = Column(Integer, primary_key=True, index=True)
    observation = Column(String(40), unique=True, index=True)
    date_reception = Column(BigInteger)
    preleveur = Column(String(100))
    controle = Column(String(100))
    client_id = Column(Integer, ForeignKey('client.idc'))
    client = relationship("Client", back_populates="demandes")
    echantillons = relationship("Echantillon",secondary=demande_echantillon)


class Echantillon(Base):
    __tablename__ = "echantillon"
    refCodebarre = Column(String(40), primary_key=True, index=True)
    id = Column(Integer,autoincrement=True)
    barcode = Column(LargeBinary(length=(2**32)-1))
    ref = Column(String(2))
    quantite = Column(Integer)
    nlot = Column(Integer)
    temperature = Column(String(20)) 
    demandes = relationship("Demande",secondary=demande_echantillon)
    parametres = relationship("Parametre",secondary=parametre_echantillon)
    natures = relationship("Nature",secondary=nature_echantillon)


class Parametre(Base):
    __tablename__ = "parametre"

    id = Column(Integer, primary_key=True, index=True)
    nomp = Column(String(40))
    echantillons = relationship("Echantillon",secondary=parametre_echantillon)
    methodes = relationship("Methode",secondary=parametre_methode)
    natures = relationship("Nature",secondary=parametre_nature)

class Methode(Base):
    __tablename__ = "methode"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String(40))
    parametres = relationship("Parametre",secondary=parametre_methode)

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
    parametres = relationship("Parametre",secondary=parametre_nature)
    echantillons = relationship("Echantillon",secondary=nature_echantillon)

    
