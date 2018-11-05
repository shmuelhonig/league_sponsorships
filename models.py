from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


engine = create_engine('sqlite:///leagues.db')
Base.metadata.create_all(engine)
