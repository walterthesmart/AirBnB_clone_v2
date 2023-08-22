#!/usr/bin/python3

""" 
The state module for HBNB project 
"""

from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
import models
from models.city import City

Base = declarative_base()

class State(BaseModel, Base):
    """ The state class """
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """This gets the attribute in case of file storage"""
            cities = models.storage.all(City)
            cities_in_state = []
            for city in cities.values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state
