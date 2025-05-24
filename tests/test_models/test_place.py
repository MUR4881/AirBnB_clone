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
        amenity_ids: list of string - empty list: it will be
        the list of Amenity.id later

"""

# Import Dependencies
from models.place import Place
from . import test_base_model

test_base_model.Model = Place


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
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)
