#!/usr/bin/python3
""" class base module """

import uuid
import datetime


class BaseModel:
    """
    class base mode
    """

    def __init__(self):
        """ init functions """
            
        self.id = str(uuid.uuid4())

        self.created_at = datetime.datetime.now();
        self.updated_at = datetime.datetime.now();

    def __str__(self):
        a = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__} "
        return a

    def save(self):
        self.updated_at = datetime.datetime.now();

    def to_dict(self):

        return self.__dict__
