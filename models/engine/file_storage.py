#!/usr/bin/python3
""" storage module """

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    clas Filestorage
    """
    def __init__(self):
        """new instance"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """all method"""
        return self.__objects

    def new(self, obj):
        """new method"""
        ki = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[ki] = obj

    def save(self):
        """serealize
        """
        dic_to_json = {}
        for key, value in self.__objects.items():
            dic_to_json[key] = value.to_dict()
        j_string = json.dumps(dic_to_json)
        with open(self.__file_path, "w") as f:
            f.write(j_string)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r') as fileJr:
                loaded_dictionary = json.loads(fileJr.read())
            for values in loaded_dictionary.values():
                execsClass = values["__class__"]
                self.new(eval(execsClass)(**values))

    @staticmethod
    def classess(self):
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        
        dic_clas = {"BaseModel" : BaseModel, "Amenity" : Amenity, "City" : City,
        "Place" : Place, "Review" : Review, "State" : State, "User" : User}