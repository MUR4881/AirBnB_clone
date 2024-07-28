#!/usr/bin/python3

# -*- coding: utf-8 -*-

""" Module which inherit from base_model and
    define place class.
"""
# Get dependencies
from base_model import BaseModel


class Place(BaseModel):
    """ Place class that define relevant ids and other variables
        and also handle place class instances.
    """
    city_id = ""  #: Holds city id
    user_id = ""  #: Holds user id
    name = ""  #: Holds name value
    description = ""  #: Holds a description
    number_rooms = 0  #: Indicate number of rooms
    number_bathrooms = 0  #: Indicate number of bathrooms
    max_guest = 0  #: Indicate number of guest room
    price_by_night = 0  #: Amount per night
    latitude = 0.0   #: Holds floating point value of latitude
    longitude = 0.0  #: Holds a floating point value of longitude
    amenity_ids = []  #: list of string of amenity ids
