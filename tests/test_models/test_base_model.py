#!/usr/bin/python3
"""Unittest for BaseModel class"""
from models.base_model import BaseModel
import models.base_model as b
import unittest
import pep8


class TestBase(unittest.TestCase):
    """Base class tests"""

    def setUp(self):
        """Base classes to the tests"""
        self.o0 = BaseModel()

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            ['models/base_model.py',
             'models/engine/file_storage.py',
             'console.py',
             'models/user.py',
             'models/state.py',
             'models/city.py',
             'models/amenity.py',
             'models/place.py',
             'models/review.py',
             'test_base.py',
             'test_user.py',
             'test_state.py',
             'test_city.py',
             'test_amenity.py',
             'test_place.py',
             'test_review.py']
        )
        self.assertEqual(
            ret.total_errors, 0,
            "Pep8 errors")

    def test_module_doc(self):
        """A test of module doc"""
        self.assertTrue(len(b.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(len(BaseModel.__doc__) > 10)

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(len(BaseModel.__init__.__doc__) > 10)


if __name__ == "__main__":
    unittest.main()
