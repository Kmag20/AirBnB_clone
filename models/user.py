#!/usr/bin/env python3
""" Defines the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class inheriting from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
