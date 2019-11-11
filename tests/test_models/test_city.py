#!/usr/bin/python3
"""Unittest for City class"""
from models.city import City
import models.city as c
import unittest
import pep8


class TestBase(unittest.TestCase):
    """City class tests"""

    def setUp(self):
        """City classes to the tests"""
        self.o0 = City()

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            [
                'tests/test_models/test_city.py',
                'models/city.py'
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
            len(City.__doc__) > 10
        )

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(
            len(City.__init__.__doc__) > 10
        )


if __name__ == "__main__":
    unittest.main()
