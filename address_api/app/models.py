from sqlalchemy import Column,Integer,String
from .database import Base

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, index=True)
    flatnum = Column(Integer)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    

