# -*- coding: utf-8 -*-

"""
    Implementation of test class for class City By extending
    the TestBaseModel class, and adding more City specific tests.
The class City:
     (models/city.py):

    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string

"""

#Import Dependencies
from models.city import City
from . import test_base_model

class TestCity(test_base_model.TestBaseModel):
    """
    """
