#!/usr/bin/python3
"""Unittest for Place class"""
from models.place import Place
import models.place as p
import unittest
import pep8


class TestBase(unittest.TestCase):
    """Base class tests"""

    def setUp(self):
        """Base classes to the tests"""
        self.o0 = Place()

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            [
                'tests/test_models/test_place.py',
                'models/place.py'
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
        self.assertTrue(len(p.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(
            len(Place.__doc__) > 10
        )

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(
            len(Place.__init__.__doc__) > 10
        )


if __name__ == "__main__":
    unittest.main()
