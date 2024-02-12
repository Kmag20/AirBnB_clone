#!/usr/bin/env python3
""" Defines the FilStorage class """


class FileStorage:
    """ represents a storage engine """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns a dictionary of __objects """
        return self.__objects

    def new(self, obj):
        """ adds <objclsname,id>:<obj> to __objects """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """    
        obj = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj, file, indent=2)

    def reload(self):
        """ deserializes the JSON file """
        try:
            with open(self.__file_path, encoding='utf-8') as file:
                dictionary = json.load(file)
                for obj in dictionary.values():
                    cls_name = obj['__class__']
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError as e:
            return
