#!/usr/bin/python3

# -*- coding: utf-8 -*-

""" Module which inherit from base_model and
    defines city class.
"""
# Get dependencies
from models.base_model import BaseModel


class City(BaseModel):
    """City class that define state variable and
        handle city instances.
    """
    state_id = ""  #: Holds the state value
    name = ""  #: Holds the name value
