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
        return self.__class__.__objects

    def new(self, obj):
        """Sets object in to the dict of objects
        with, the object id as it key

        Args:
            obj: Reference/identifier to the object to be stored
        """
        if isinstance(self.__objects, dict):
            """ Check the file_name if it is a dictionary """
            # Storing object with the <obj class name>.id as key
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        # if object is not a type dictionary
        else:
            pass

    def save(self):
        """Serializes __objects to the JSON file(__file_path)
        """

        serial_dict = {}  #: dict: dict/Buffer to store, dict of objects
        # Generate Serializeable dict representation of the objects
        for key in self.__objects:
            serial_dict[key] = self.__objects[key].to_dict()
        
        if isinstance(self.__file_path, str):
            """ Check if the file_path name is a string. """
            # Open the file
            with open(self.__file_path, 'w', encoding='utf-8') as Jfile:
            # Now write serialize directly into the file
                dump(serial_dict, Jfile)
        # if file_path is not a type string            
        else:
            pass

    def reload(self):
        """Deserialize the JSON file (__file_path) to __objects
        only if the json file exist otherwise, do nothing,
        if the file doesn't exit, no exception should be raised
        """
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
