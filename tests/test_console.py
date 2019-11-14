#!/usr/bin/python3
"""Unittest for BaseModel class.."""
from models.base_model import BaseModel
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models.base_model as b
import unittest
import pep8


class TestBase(unittest.TestCase):
    """Base class tests"""

    def setUp(self):
        """Base classes to the tests"""
        self.o0 = HBNBCommand()

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            [
                'tests/test_models/test_base_model.py',
                'models/__init__.py',
                'models/engine/__init__.py',
                'tests/__init__.py',
                'tests/test_models/__init__.py',
                'tests/test_models/test_engine/__init__.py'
            ]
        )
        p8.options.report.print_statistics()
        self.assertEqual(
            ret.total_errors,
            0,
            "Pep8 errors"
        )

    def test_module_doc(self):
        """A test of module doc"""
        self.assertTrue(len(b.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(
            len(BaseModel.__doc__) > 10
        )

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(
            len(BaseModel.__init__.__doc__) > 10
        )

    def test_str(self):
        """A test of __str__ method"""
        self.assertTrue(
            len(BaseModel.__str__.__doc__) > 10
        )

    def test_repr(self):
        """A test of __repr__ method"""
        self.assertTrue(
            len(BaseModel.__repr__.__doc__) > 10
        )

    def test_base_model_save(self):
        """A test of save method"""
        self.assertTrue(
            len(BaseModel.save.__doc__) > 10
        )

    def test_base_model_to_dict(self):
        """A test of to_dict method"""
        self.assertTrue(
            len(BaseModel.to_dict.__doc__) > 10
        )

    def test_update_from_diccionary(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.o0.onecmd("help show")
        print(f)


if __name__ == "__main__":
    unittest.main()
