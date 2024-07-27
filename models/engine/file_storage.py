#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A module for the FileStorage class, which contains method
    that take care of methods responsible for:
    Serialization/De-Serialization/and Storage and retriever of
    objects
"""
# Importing Dependecies
from json import loads, dump
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and
    Deserializes JSON file to instances.
    """
    __file_path = "file.json"  #: str: The path to file, for storage
    __objects = {}  #: dict: dictionary to store all objects

    def all(self):
        """Return a dictionary containing all objects
        """
        # Converting to an empty dict if wasn't a dict
        if not isinstance(self.__objects, dict):
            self.__class__.__objects = {}
        return self.__objects

    def new(self, obj):
        """Sets object in to the dict of objects
        with, the object id as it key

        Args:
            obj: Reference/identifier to the object to be stored
        """
        # convert it to a dictionary instead if is not!
        # That is better, since we still have to store objects
        if not isinstance(self.__objects, dict):
            self.__class__.__objects = {}
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file(__file_path)
        """

        serial_dict = {}  #: dict: dict/Buffer to store, dict of objects
        # Generate Serializeable dict representation of the objects
        for key in self.__objects:
            serial_dict[key] = self.__objects[key].to_dict()
        # Thinking of overwriting the file_path instead of skipping?
        if isinstance(self.__file_path, str) and len(self.__file_path):
            """ Check if the file_path name is a string. """
            # Open the file
            with open(self.__file_path, 'w', encoding='utf-8') as Jfile:
                # Now write serialize directly into the file
                dump(serial_dict, Jfile)
        # if file_path is not a type string

    def reload(self):
        """Deserialize the JSON file (__file_path) to __objects
        only if the json file exist otherwise, do nothing,
        if the file doesn't exit, no exception should be raised
        """
        # Just Return, if the file_path is not string or str of length zero
        if (type(self.__file_path) is not str) or (len(self.__file_path) == 0):
            return
        # Open the file, if it exits
        try:
            with open(self.__file_path) as file:
                # Converting file content to python object
                json_string = file.read()  # To prevent passing an empty
                if len(json_string) >= 2:  # ensuring not empty
                    obj_dicts = loads(json_string)
                else:
                    obj_dicts = {}

        except FileNotFoundError:
            pass
        # if eventually,file was opened
        else:
            # Now Reloading
            for key, obj_dict in obj_dicts.items():
                self.__objects[key] = eval(obj_dict['__class__'])(**obj_dict)
