# -*- encoding: utf-8 -*-

"""Implemetation of test suites for the BaseModel class.

The BaseModel class:
    * Defines all common/methods for other classes

    * public instance attributes:
        * id: string - assign with an uuid when an instance is created:
            * uuid.uuid4() is used to generate unique id (string format)
            * The goal is to have unique id for each BaseModel
        * created_at: datetime - assign with the current datetime when an
        instance is created

        * updated_at: datetime - assign with the current datetime when an
        instance is created and it will be updated every time you change your
        object
    * __str__: should print: [<class name>] (<self.id>) <self.__dict__>

    * Public instance methods:

        * save(self): updates the public instance attribute updated_at with
        current datetime
        * to_dict(self): returns a dictionary containing all keys/values of
        __dict__ of the instance:
            * by using self.__dict__, only instance attributes set will be
            returned
            * a key __class__ must be added to this dictionary with the class
            name of the object
            * created_at and updated_at must be converted to string object
            in ISO formart:
                * format: "%Y-%m-%d%H:%M%S.%f"
                * You can use isoformat() of datetime object

"""
# import the class to be tested
from models.base_model import BaseModel
# import the test module
import unittest
import datetime
import uuid


Model = BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing all the functionalities of the
    BaseModel class to be sure, they all work
    """

    print(Model)

    def test_attributes(self):
        '''Test that common attributes exits
        '''
        test_model = Model()
        self.assertCountEqual(['id', 'created_at', 'updated_at'],
                              test_model.__dict__.keys())

    def test_to_dict(self):
        '''Test the to_dict functionality
        '''
        created_at = datetime.datetime.now().isoformat()
        test_model = Model(id=uuid.uuid4(), created_at=created_at,
                           updated_at=created_at,
                           name="My First Model", my_number=89, age=11)
        self.assertCountEqual(['id', 'created_at', 'updated_at', '__class__',
                               'name', 'my_number', 'age'],
                              test_model.to_dict().keys())

    def test_attributes2(self):
        """Test attributes for
        """
        test_model = Model()
        self.assertEqual(test_model.created_at.isoformat()[:-7],
                         datetime.datetime.now().isoformat()[:-7])

    def test_timestamp(self):
        '''Testing that created_at is same as updated_at
        '''
        test_model = Model()
        self.assertEqual(test_model.created_at, test_model.updated_at,
                         "Confirmed to be same")

    def test_save(self):
        '''Test the save functionality
        '''
        test_model = Model()
        test_model.save()  # checking to see if saving, updates the updated_at
        self.assertNotEqual(test_model.created_at, test_model.updated_at,
                            "Save does update created_at?")

    def test__str__(self):
        '''Testing the string representation of the object
        '''
        test_model = Model()
        self.assertEqual(f"[{test_model.__class__.__name__}] ({test_model.id})"
                         f" {test_model.__dict__}",
                         test_model.__str__())

    def test_update(self):
        '''Test update functionality of the BaseModel objects
        '''
        test_model = Model()
        test_model.name = "Who"
        test_model.update('name', 'yes')
        self.assertEqual(test_model.name, 'yes')

    def test_from_dict(self):
        """Test creating, the object from dictionary using
        (implemented use **kwargs) arguement passed to the
        BaseModel class
        """

        dct = {"id": str(uuid.uuid4()),
               "created_at": datetime.datetime.now().isoformat(),
               "updated_at": datetime.datetime.now().isoformat(),
               "name": "Bool_shit", "__class__": Model.__name__}
        test_model = Model(**dct)
        self.assertDictEqual(test_model.to_dict(), dct)
