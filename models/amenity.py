#!/usr/bin/python3
""" The amenity Module of AirBnB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
        This class defines amenities by various attributes

        Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities
        name (sqlalchemy String): The name of the Amenity (max 128 characters)
        place_amenities (sqlalchemy.orm.relationship): A list of places
        associated with the Amenity
"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity',
                                   viewonly=False)
