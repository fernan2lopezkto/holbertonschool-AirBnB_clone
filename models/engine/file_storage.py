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

        jojojo = []
        for key in self.__objects:
            jojojo.append(self.__objects[key].BaseModel.to_dict())

        j_string = json.dumps(jojojo)

        with open(self.__file_path, "w") as f:
            f.write(j_string)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
