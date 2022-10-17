#!/usr/bin/python3
"""amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class"""
    def __init__(self):
        """cons method"""
        self.name = ""
