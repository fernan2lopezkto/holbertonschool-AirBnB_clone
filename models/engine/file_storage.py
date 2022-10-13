#!/usr/bin/python3
""" storage module """
import os
import json


class FileStorage:
    """ 
    that serializes instances
    to a JSON file and deserializes
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
        """
        serializes __objects to
        the JSON file (path: __file_path)
        """
        j_string = json.dumps(self.__objects)

        with open(self.__file_path, "w") as f:
            return f.write(j_string)

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
