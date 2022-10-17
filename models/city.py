#!/usr/bin/python3
""" city module """

from models.base_model import BaseModel


class City(BaseModel):
    """city class"""
    def __init__(self):
        self.name = ""
        self.state_id = ""
