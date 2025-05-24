# -*- coding: utf-8 -*-

"""
    Implementation of test class for class Place By extending
    the TestBaseModel class, and adding more Place specific tests.
The class Place:
    (models/place.py):

    Public class attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list: it will be the list of Amenity.id later

"""

#Import Dependencies
from models.place import Place
from . import test_base_model

test_base_model.__dict__["Model"] = Place

class TestPlace(test_base_model.TestBaseModel):
    """
    Test Class Which implemnt test cases
    and test suite for the class Place
    """
    def test_public_var_type(self):
        """
        Method to check and verify(test)
        type of class attributes
        """
        self.assertIsInstance(f"Place.__dict__['city_id']", str)
        self.assertIsInstance(f"Place.__dict__['user_id']", str)
        self.assertIsInstance(f"Place.__dict__['name']", str)
        self.assertIsInstance(f"Place.__dict__['description']", str)
        print(type(f"Place.__dict__['number_rooms']"))
        self.assertIsInstance(f"Place.__dict__['number_rooms']", int)
        self.assertIsInstance(f"Place.__dict__['number_bathrooms']", int)
        self.assertIsInstance(f"Place.__dict__['max_guest']", int)
        self.assertIsInstance(f"Place.__dict__['price_by_night']", int)
        self.assertIsInstance(f"Place.__dict__['latitude']", float)
        self.assertIsInstance(f"Place.__dict__['longitude']", float)
        self.assertIsInstance(f"Place.__dict__['amenity']", list)

