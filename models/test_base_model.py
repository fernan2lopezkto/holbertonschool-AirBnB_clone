#!/usr/bin/python3
from base_model import BaseModel
import time


my_model = BaseModel()

print()

print(my_model)

print()

print(type(my_model.created_at))
print(type(my_model.updated_at))


print(my_model.created_at)

print(my_model.updated_at)


time_duration = 3
time.sleep(time_duration)

print()

my_model.save()

print(my_model.created_at)
print(my_model.updated_at)

print(my_model.to_dict())

"""print(my_model)
"""