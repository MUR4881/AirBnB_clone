#!/usr/bin/python3

# -*- encoding: utf-8 -*-

"""Test Cases for the FileStorage class
The class FileStorage serializes instances to a JSON file and
deserialize JSON file to instances:

    * models/engine/file_storage.py
    * Private class attributes:
        * __file_path: string - path to the JSON file (ex: file.json)
        * __objects: dictionary - empty but will store all objects by
        <class name>.id e.g BaseModel.1212121212
    * Public instance methods:
        * all(self): returns the dictionary __objects
        * new(self, obj): sets in __objects the obj with
        key <obj class name>.id
        * save(self): deserializes the JSON file to __objects
        (only if the JSON file (__file_path)exists; otherwise,
        do nothing. If the file doesn't exist, no exception should
        be raised
"""
# Import dependencies
import os
# Import the test framework
import unittest
# Import the class to be tested
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Testing the file storage engine
    """

    def test__objects(self):
        """Test if, the __objects dict is not empty
        after reload
        """
        try:
            os.stat("file.json")
            storage = FileStorage()
            storage.reload()
            self.assertGreater(len(storage.all()), 0)
        except FileNotFoundError:
            self.skipTest("Json file not in found")

    def test_new(self):
        """Testing the new() functionality of FileStorage
        class
        """
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        bm.save()  #  storage.save() is called by this method
        storage.reload()
        self.assertTrue(f"{bm.__class__.__name__}.{bm.id}"
                        in storage.all(), "Deserialization Failed")
