#!/usr/bin/python3

# -*- coding: utf-8 -*-

""" Module which inherit from base model and defines/
    implement the review class
"""
# Get dependencies
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review which review user and place id
        and handle instances of the class
    """
    place_id = ""  #: Holds value of place id
    user_id = ""  #: Holds user id
    text = ""  #: Holds the text
