#!/usr/bin/python3
# Defines a city model.
# Inherits from SQLAlchemy Base and links to the MySQL table cities.

from sqlalchemy import Column, Integer, String, Foreignkey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
