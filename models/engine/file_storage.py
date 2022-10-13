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
        jojojo = []
        for key in self.__objects:
            a = self.__objects[key]

            b = to_dict_storage(a)

            jojojo.append(b)

        j_string = json.dumps(jojojo)

        with open(self.__file_path, "w") as f:
            f.write(j_string)

    def reload(self):
        """deserializes
        """
        if os.path.exists(self.__file_path):

            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)

def to_dict_storage(ki_obj):
    ki_atr_ibuts = ki_obj.__dict__
    jojojo = {}

    for key in ki_atr_ibuts.keys():
        if key == "created_at" or key == "updated_at":
            a = ki_atr_ibuts[key].isoformat()
            jojojo[key] = a
        else:
            jojojo[key] = ki_atr_ibuts[key]
        jojojo["__class__"] = ki_obj.__class__.__name__

    return jojojo