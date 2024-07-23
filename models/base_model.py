#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A module to be used for the backend of a web project
AirBnB clone!
This module is meant to contain a BaseModel, that contains
attributes and methods relating to different classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A Base class containing attributes related to multiple
    other/subclasses.
    """

    def __init__(self):
        '''Initializing a new instance
        '''
        self.id = str(uuid4())  #: str: A unique id for the object
        self.created_at = datetime.now()  #: Time object was created
        self.updated_at = self.created_at  #: Time object was updated last

    def __str__(self):
        """Generate a string representation of the instance/object

        Return: A string representation of the obj/instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates teh public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Generate a dictionary containing all attribute
        and type of an object
        """
        new_dict = self.__dict__.copy()  #: dict: a copy of the obj attr
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
