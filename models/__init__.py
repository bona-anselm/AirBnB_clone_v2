#!/usr/bin/python3
"""
    This module instantiates an object of class FileStorage

    If the environment variable 'HBNB_TYPE_STORAGE' is set to 'db',
    it instantiates a database storage engine (DBStorage).

    Otherwise, it instantiates a file storage engine (FileStorage).
"""
from os import getenv
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
