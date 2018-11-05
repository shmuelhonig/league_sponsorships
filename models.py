from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Leagues(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    latitude = Column(Float)
    longitude = Column(Float)
    price = Column(Integer)


engine = create_engine('sqlite:///leagues.db')
Base.metadata.create_all(engine)
