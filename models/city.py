#!/usr/bin/python3
""" City Module for AirBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel, Base):
    """
        The city class, contains state ID and name. Inherits from
        BaseModel, Base and links to the MySQL table cities

        Attributes:
        __tablename__ (str): MySQL table to store the City
        name (sqlalchemy.String): The name of the City
        state_id (sqlalchemy.String): The state id of the City
        places (sqlalchemy.orm.relationship): A list of places within
        the City
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
