#!/usr/bin/python3

""" The review script for the HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ The review class to store review information """
    __tablename__ = "reviews"

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
