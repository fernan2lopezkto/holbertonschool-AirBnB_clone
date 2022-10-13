#!/usr/bin/python3
""" class base module """

import uuid
import datetime
from models import storage


class BaseModel:
    """
    class base mode
    """

    def __init__(self, *args, **kwargs):
        """ init functions """

        if len(kwargs) == 0:
            
            self.id = str(uuid.uuid4())

            self.created_at = datetime.datetime.now();
            self.updated_at = datetime.datetime.now();

            storage.new
        else:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        m = kwargs[key]
                        datetime.datetime.strptime(m, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, kwargs[key])

    def __str__(self):
        a = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__} "
        return a

    def save(self):
        self.updated_at = datetime.datetime.now();
        storage.save()

    def to_dict(self):

        self_atr_ibuts = self.__dict__
        jojo = {}

        for key in self_atr_ibuts.keys():
            if key == "created_at" or key == "updated_at":
                a = self_atr_ibuts[key].isoformat()
                jojo[key] = a
            else:
                jojo[key] = self_atr_ibuts[key]
            jojo["__class__"] = self.__class__.__name__

        return jojo
