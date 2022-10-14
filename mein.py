#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
print("objto creado")
my_model.name = "My_First_Model"
my_model.my_number = 865
print("se le agrego cosas al objeto")
my_model.save()
print("se le hizo un cambio")
print(my_model)
