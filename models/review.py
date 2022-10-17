#!/usr/bin/python3
"""review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class
    """
    def __init__(self):
        """cons method"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
