from sqlalchemy import select,and_
from sqlalchemy.orm import Session
import models


def get_association_parametre_methode(db: Session, idp :int,idm :int):
    association = select(models.parametre_methode).where(and_(models.parametre_methode.c.parametre_id == idp, models.parametre_methode.c.methode_id == idm))
    db.execute(association)
    db.commit()
    return association


def get_association_parametre_nature(db: Session, idp :int,idn :int):
    association = select(models.parametre_nature).where(and_(models.parametre_nature.c.parametre_id == idp, models.parametre_nature.c.nature_id == idn))
    db.execute(association)
    db.commit()
    return association

def create_association_parametre_methode(db: Session, idp :int,idm :int):
    association = models.parametre_methode.insert().values(parametre_id= idp, methode_id=idm)
    db.execute(association)
    db.commit()
    return True


def create_association_parametre_nature(db: Session, idp :int,idn :int):
    association = models.parametre_nature.insert().values(parametre_id= idp, nature_id=idn)
    db.execute(association)
    db.commit()
    return True