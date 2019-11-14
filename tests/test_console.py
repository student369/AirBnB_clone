#!/usr/bin/python3
"""Unittest for the HBNBCommand class."""
from models.base_model import BaseModel
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import console as c
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
                'tests/test_console.py',
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
        self.assertTrue(len(c.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(
            len(HBNBCommand.__doc__) > 10
        )

    def test_quit(self):
        """A test of do_quit method"""
        self.assertTrue(
            len(HBNBCommand.do_quit.__doc__) > 10
        )

    def test_eof(self):
        """A test of EOF method"""
        self.assertTrue(
            len(HBNBCommand.do_EOF.__doc__) > 10
        )

    def test_emptyline(self):
        """A test of save method"""
        self.assertTrue(
            len(HBNBCommand.emptyline.__doc__) > 10
        )

    def test_do_create(self):
        """A test of do_create method"""
        self.assertTrue(
            len(HBNBCommand.do_create.__doc__) > 10
        )

    def test_do_destroy(self):
        """A test of do_create method"""
        self.assertTrue(
            len(HBNBCommand.do_destroy.__doc__) > 10
        )

    def test_do_update(self):
        """A test of do_update method"""
        self.assertTrue(
            len(HBNBCommand.do_update.__doc__) > 10
        )


if __name__ == "__main__":
    unittest.main()
