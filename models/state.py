#!/usr/bin/python3

# -*- coding: utf-8 -*-

""" Module that inherit from base class and define
    the state class to handle state instances.
"""
# Import dependencies
from models.base_model import BaseModel


class State(BaseModel):
    """ State class to handle name attribute
        and handle state instances.
    """
    name = ""  #: Hold the name variable value
