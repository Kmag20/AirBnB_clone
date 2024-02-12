#!/usr/bin/env python3
""" Defines the BaseModel """
import uuid
import datetime

class BaseModel:
    def __init__(self):
        """ represents the basemodel class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ prints a formal string representation of an instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """ updates the public instance attrib with current time """
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
