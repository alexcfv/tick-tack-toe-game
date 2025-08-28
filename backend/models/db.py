from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

#Экранирование не нужно, использую orm

metadata = MetaData()
Base = declarative_base()

load_dotenv()

def db_connect(testing=False):
    
    if testing:
        username = os.getenv("TEST_DATABASE_USERNAME")
        password = os.getenv("TEST_DATABASE_PASSWORD")
        dbname = os.getenv("TEST_DATABASE_NAME")
        port = os.getenv("TEST_DATABASE_PORT")
        host = os.getenv("TEST_DATABASE_HOST")
        
    else:
        username = os.getenv("DATABASE_USERNAME")
        password = os.getenv("DATABASE_PASSWORD")
        dbname = os.getenv("DATABASE_NAME")
        port = os.getenv("DATABASE_PORT")
        host = os.getenv("DATABASE_HOST")

    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}", echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    return engine, SessionLocal

def create_tables(local_engine):
    metadata.drop_all(local_engine, checkfirst=True)
    metadata.create_all(local_engine, checkfirst=True)


def create_tables_orm(local_engine):
    Base.metadata.drop_all(local_engine, checkfirst=True)
    Base.metadata.create_all(local_engine, checkfirst=True)


def create_session(local_engine):
    Session = sessionmaker(local_engine)
    session = Session()

    return session