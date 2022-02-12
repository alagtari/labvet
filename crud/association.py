from sqlalchemy.orm import Session
import models



def create_association_parametre_methode(db: Session, idp :int,idm :int):
    insert = False
    try:
        association = models.parametre_methode.insert().values(parametre_id= idp, methode_id=idm)
        db.execute(association)
        db.commit()
        insert = True
    except Exception as e:
        pass
    
    return insert


def create_association_parametre_nature(db: Session, idp :int,idn :int):
    insert = False
    try:
        association = models.parametre_nature.insert().values(parametre_id= idp, nature_id=idn)
        db.execute(association)
        db.commit()
        insert = True
    except Exception as e:
        pass
    
    return insert