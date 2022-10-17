#!/usr/bin/python3
"""Base Model"""

import datetime
import models
from uuid import uuid4


class BaseModel():
    """new base model"""

    def __init__(self, *args, **kwargs):
        """new intance"""
        if kwargs:
            for element, value in kwargs.items():
                if element in ("created_at", "updated_at"):
                    tim = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.datetime.strptime(value, tim)
                if element != "__class__":
                    setattr(self, element, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """rewrite __str__"""
        a = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__} "
        return a

    def save(self):
        """save method
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict method"""
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
