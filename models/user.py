#!/usr/bin/python3
"""interpreter"""

from models.base_model import BaseModel


class User(BaseModel):
    """class user that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
