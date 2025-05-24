# -*- coding: utf-8 -*-

"""
    Implement Test Class For Class Review
The Class Review:
     (models/review.py):

    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
"""

# Import Dependencies
from models.review import Review
from tests.test_models import test_base_model

test_base_model.__dict__["Model"] = Review


class TestReview(test_base_model.TestBaseModel):
    """
    Unit test the Review Class by implementing
    test cases and test suite
    """
    def test_public_var_type(self):
        """
        Method to unit test publc class attributes
        """
        self.assertIsInstance(f"Review.__dict__['place_id']", str)
        self.assertIsInstance(f"Review.__dict__['user_id']", str)
        self.assertIsInstance(f"Review._-dict__['text']", str)
