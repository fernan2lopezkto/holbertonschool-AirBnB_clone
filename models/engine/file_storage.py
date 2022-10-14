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
        print("hola")

        if os.path.exists(self.__file_path):

            print("the file exist")
            with open(self.__file_path, "r") as f:

                print("open it")

                string_list_obgets = json.load(f)

                print(type(string_list_obgets))
                print(type(string_list_obgets[0]))
                print(string_list_obgets)

                for itm in string_list_obgets:
                    print(itm)
                    print(type(itm))
                    a = itm['id']
                    print(a)
                    print()
                    kisss = f"{itm['__class__']}.{itm['id']}"
                    self.__objects[kisss] = itm

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
 