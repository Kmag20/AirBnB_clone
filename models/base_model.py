#!/usr/bin/env python3
""" Defines the BaseModel class """
import datetime
import uuid


class BaseModel:
    """ BaseModel class of the entire project """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Returns an informal representation of an instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ Updates the public instance attribute """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dict containing all key/value """
        dict = {}

        for key, value in self.__dict__.items():
            if value.__class__.__name__ == 'datetime':
                value = value.isoformat()
            dict.__setitem__(key, value)

        dict.__setitem__('__class__', self.__class__.__name__)
        return dict
