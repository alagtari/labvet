from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/labvet" 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True,
)

if not database_exists(engine.url):
    create_database(engine.url)


SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()

