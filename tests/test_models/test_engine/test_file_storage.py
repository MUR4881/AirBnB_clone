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
        * save(self): serializes __objects to the JSON file(path:__file_path)
        * reload(self): deserializes the JSON file to __objects
        (only if the JSON file (__file_path)exists; otherwise,
        do nothing. If the file doesn't exist, no exception should
        be raised
"""
# Import dependencies
import os
from sys import stderr
# Import the test framework
import unittest
# Import the class to be tested
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Testing the file storage engine
    """
    @classmethod
    def setUpClass(cls):
        """Create a storage object for tests
        """
        try:
            os.stat("file.json")
        except FileNotFoundError:
            # self.skipTest("Json file not in found")
            print("Json File Not Found\nCreating One", file=stderr)
            for i in range(1, 1001):  # Creating objects if none exist before
                bm = BaseModel()
                bm.name = f"User:{i}"
            bm.save()  # Save all objects, this save called FileStorage save
        finally:
            cls.storage = FileStorage()
            cls.storage.reload()

    def setUp(self):
        """Create a model for each test
        """
        self.object = BaseModel()

    def test_reload(self):
        """Testing the reload functionality serializes
        correctly
        """
        self.storage.reload()
        self.assertTrue(self.storage.all())  # confirm objects were reloaded

    def test_all(self):
        """Test the all functionality
        """
        self.assertTrue(self.storage.all())

    def test_save(self):
        """Test the save functionality
        """
        prev_len = len(self.storage.all())
        bm = BaseModel()
        bm.save()
        new_len = len(self.storage.all())
        self.assertEqual(new_len, prev_len + 1, msg="Object not saved")

    def test__objects_not_empty(self):
        """Test if, the __objects dict is not empty
        after reload, obviously a test for `reload`
        """
        self.assertGreater(len(self.storage.all()), 0)

    def test_new(self):
        """Testing the new() functionality of FileStorage
        class
        """
        bm = self.object
        # self.storage.new(bm) new is automatically invoked
        bm.save()  # storage.save() is called by this method
        # Testing the new functionality
        self.storage.reload()
        self.assertTrue(f"{bm.__class__.__name__}.{bm.id}"
                        in self.storage.all(), "Deserialization Failed")

    def test_new_int(self):
        """Test the new functionality, with Integer object
        """
        with self.assertRaises(AttributeError):
            self.storage.new(int(1234))

    def test_new_str(self):
        """Test the new functionality with string object
        """
        with self.assertRaises(AttributeError):
            self.storage.new(str(1234))
