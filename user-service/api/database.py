import sqlalchemy
from sqlalchemy.orm import sessionmaker

from api.models.sqlmodels import Base

db_url = 'sqlite:///user.db'

engine = sqlalchemy.create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)


def create_tables():
    Base.metadata.create_all(engine)
