#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): column of an auto_generated, unique integer
        name(str): column of string of 128 characters 
        state_id(int): the state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

