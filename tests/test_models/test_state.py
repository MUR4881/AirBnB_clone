# -*- coding: utf-8 -*-

"""
    Implementing Test Class for State Class:

The State Class:
    (models/state.py):

    Public class attributes:
        name: string - empty string
"""

#Import Dependencies
from models.state import State
from tests.test_models import test_base_model

test_base_model.__dict__["Model"] = State

class TestState(test_base_model.TestBaseModel):
    """
    Unit testing State Class by writtting unit
    test cases and test suite for each edge case
    """
    def test_public_var_type(self):
        """
        Method that implement test suites
        to ensure a consistent class attribute type
        """
        self.assertIsInstance(f"State.__dict__['name']", str)
