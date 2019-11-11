#!/usr/bin/python3
"""Unittest for State class"""
from models.state import State
import models.state as s
import unittest
import pep8


class TestBase(unittest.TestCase):
    """State class tests"""

    def setUp(self):
        """State classes to the tests"""
        self.o0 = State()

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            [
                'tests/test_models/test_state.py',
                'models/state.py'
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
        self.assertTrue(len(s.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(
            len(State.__doc__) > 10
        )

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(
            len(State.__init__.__doc__) > 10
        )


if __name__ == "__main__":
    unittest.main()
