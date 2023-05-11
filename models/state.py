#!/usr/bin/python3
""" State Module for AirBnB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models import City


class State(BaseModel, Base):
    """
        This class represents a state

        It inherits from BaseModel and Base, and creates a relationship
        with City

        Attributes:
        __tablename__ (str): The name of the MySQL table to store States
        name (sqlalchemy.String): The name of the state (max 128 characters)
        cities (sqlalchemy.orm.relationship): The cities related to the state
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list
    else:
        cities = relationship("City", backref="state", cascade="delete")
