#!/usr/bin/python3
"""Unittest for Amenity class"""
from models.amenity import Amenity
import models.amenity as a
import unittest
import pep8


class TestBase(unittest.TestCase):
    """State class tests"""

    def setUp(self):
        """Amenity classes to the tests"""
        self.o0 = Amenity()

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            [
                'tests/test_models/test_amenity.py',
                'models/amenity.py'
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
        self.assertTrue(len(a.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(
            len(Amenity.__doc__) > 10
        )

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(
            len(Amenity.__init__.__doc__) > 10
        )


if __name__ == "__main__":
    unittest.main()
