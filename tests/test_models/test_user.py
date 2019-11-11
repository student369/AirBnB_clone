#!/usr/bin/python3
"""Unittest for User class"""
from models.user import User
import models.user as u
import unittest
import pep8


class TestBase(unittest.TestCase):
    """Tests for User class"""

    def setUp(self):
        """User classes to test"""
        self.o0 = User()

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            [
                'tests/test_models/test_user.py',
                'models/user.py'
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
        self.assertTrue(len(u.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(
            len(User.__doc__) > 10
        )

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(
            len(User.__init__.__doc__) > 10
        )


if __name__ == "__main__":
    unittest.main()
