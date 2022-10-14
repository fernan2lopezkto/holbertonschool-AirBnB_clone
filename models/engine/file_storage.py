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
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        ki = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[ki] = obj

    def save(self):
        """serealize
        """
        dic_to_json = {}
        """create a dictionary to serializate"""

        for key, value in self.__objects.items():            
            dic_to_json[key] = value.to_dict()

        j_string = json.dumps(dic_to_json)

        with open(self.__file_path, "w") as f:
            f.write(j_string)

    def reload(self):
        """deserializes
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                dict_obgets_from_json = json.load(f)
                for itm in dict_obgets_from_json:
                    self.__objects[itm] = BaseModel(itm)
