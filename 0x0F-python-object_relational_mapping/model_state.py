#!/usr/bin/python3
# Inherits from SQLAlchemy Base
# Links to the MySQL table states
# Define a state mode

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)

