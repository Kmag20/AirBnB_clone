#!/usr/bin/env python3
"""  class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Represents the FileStorage Class """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        obj = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj, file, indent=2)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) """
        try:
            with open(self.__file_path, encoding='utf-8') as file:
                dictionary = json.load(file)
                for obj in dictionary.values():
                    cls_name = obj['__class__']
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError as e:
            return
