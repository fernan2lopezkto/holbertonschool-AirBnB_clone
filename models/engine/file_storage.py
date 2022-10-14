#!/usr/bin/python3
""" storage module """
import os
import json


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
        print("start save in storage")
        dic_to_json = {}
        for key in self.__objects:
            print(type(key))
            print(type(self.__objects[key]))
            obj_e = self.__objects[key]
            print(type(obj_e))
            print(obj_e)
            dic_to_json[key] = self.__objects

        j_string = json.dumps(dic_to_json)

        with open(self.__file_path, "w") as f:
            f.write(j_string)
        print("save ok")

    def reload(self):
        """deserializes
        """

        if os.path.exists(self.__file_path):
            """open fil """
            with open(self.__file_path, "r") as f:
                """write file as r mode"""
                dict_obgets_from_json = json.load(f)
                """make a dictionary from json file (deserealized)"""
                for itm in dict_obgets_from_json:
                    """itm is a dict in to the dict_obgets_from_json"""
                    from models.base_model import BaseModel
                    """import to use BaseModel"""
                    self.__objects[itm] = BaseModel(itm)
                    """set in __obgets any itm BaseModel instances
                    """
