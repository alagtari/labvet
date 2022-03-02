from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://ihewufbs_labvetadmin:labvetebuild1@102.219.176.39:3306/ihewufbs_labvet" 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True,
)



SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()

