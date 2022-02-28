from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://uoqyelw7zfmuesfp:en1cpR26hNiBhJbMuvaq@b5dhx5x07ktx2d4nkl47-mysql.services.clever-cloud.com:3306/b5dhx5x07ktx2d4nkl47" 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True,
)



SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()

