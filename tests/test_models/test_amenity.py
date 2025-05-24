# -*- encoding: utf-8 -*-

"""
Implementation of test class for class Amenity By extending
the TestBaseModel class, and adding more Amenity specific tests.

The class Amenity:
    Amenity (models/amenity.py):

    Public class attributes:
        name: string - empty string

"""

from models.amenity import Amenity
from tests.test_models import test_base_model

# Changing the Modules global variable, called Model, which is used by
# the Test Classes so the test can be performed on our desired classes

test_base_model.__dict__["Model"] = Amenity

# print(TestBaseModel.__dict__)


class TestAmenity(test_base_model.TestBaseModel):
    """
        Importing from TestBaseModel, which include the basic test
        cases and also improving the Amenity test cases
    """

    def test_public_var_type(self):
        """
            Test the public class attribute of the
            Associated class(TestAmenity).
            """
        self.assertIsInstance(f"Amenity.__dict_.['name']", str)
