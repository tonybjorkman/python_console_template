from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Add classes to be included in the DB schema below
class Cat(Base):
    __tablename__ = "cat"
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    age = Column(Integer)


