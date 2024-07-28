#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""user module housing a User class that inherits from
BaseModel class, which hold, useful methods
"""
# Get Dependencies
from models.base_model import BaseModel


class User(BaseModel):
    """User class that hold user attributes, like names
    and more.
    """
    email = ""  #: str: Email of course!
    password = ""  #: str: user's password
    first_name = ""  #: str: user's first_name
    last_name = ""    #: str: user's last_name
