#!/usr/bin/python3
""" class base module """

import uuid
import datetime
import time


class BaseModel:
    """
    class base mode
    """

    id = str(uuid.uuid4())

    @property()
    def created_at(self):
        created_at = datetime.date.fromtimestamp(time.time());
        return created_at

    updated_at = datetime.date.fromtimestamp(time.time());

    def __str__(self):
        a = f"[BaseModel] ({self.id}) {self.__dict__} "
        return a

    def save(self):
        updated_at = datetime.date.fromtimestamp(time.time());

    def to_dict(self):
        item_needed = ["id", "created_at", "updated_at"]
        self_atrib = self.__dict__
        filt_atrib = {}

        for itm in range(len(self_atrib)):
            filt_atrib[item_needed[itm]] = getattr(self, item_needed[itm])

        return filt_atrib
        