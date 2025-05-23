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

test_base_model.__dict__["Model"] = City

class TestCity(test_base_model.TestBaseModel):
    """
    Class Which Implement test cases and
    test suite for the class City
    """
    def test_public_var_type(self):
        """
        The method to ensure the public class attribute
        has a consistent type
        """
        self.assertIsInstance(f"City._-dict__['name']", str)
        self.assertIsInstance(f"City.__dict__['state_id']", str)
