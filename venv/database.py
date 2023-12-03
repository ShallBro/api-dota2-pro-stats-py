from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()


class Heroes(Base):
    __tablename__ = "heroes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    images = Column(String)


def connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
