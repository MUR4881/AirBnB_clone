#!/bin/python3

# -*- coding: utf-8 -*-

"""
    Implementing Test Class for Class User.
The class User:

    models/user.py
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string

"""

# Importing dependencies
from models.user import User
from . import test_base_model

test_base_model["Model"] = User

class TestUser(test_base_model.TestBaseModel):
    """
    Unit test class which implemebt test cases and
    test suite for User class
    """
