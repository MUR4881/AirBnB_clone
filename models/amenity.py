#!/usr/bin/python3

# -*- coding: utf-8 -*-

""" Module that inherit from base_model and
    define Amenity class
"""
# Import dependencies
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity which handles the name variable
        and instances of the class.
    """
    name = ""  #: Holds name variable value
