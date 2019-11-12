#!/usr/bin/python3
"""Unittest for BaseModel class."""
from models.engine import file_storage as f
import unittest
import pep8


class TestFileStorage(unittest.TestCase):
    """Base class tests"""

    def setUp(self):
        """Base classes to the tests"""
        self.o0 = f.FileStorage()

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            [
                'tests/test_models/test_file_storage.py',
                'models/engine/file_storage.py'
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
        self.assertTrue(len(f.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(
            len(f.FileStorage.__doc__) > 10
        )

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(
            len(f.FileStorage.__init__.__doc__) > 10
        )

    def test_private_file_path(self):
        """Test the file path private attribute"""
        with self.assertRaises(AttributeError):
            self.oO.__file_path

    def test_private_objects(self):
        """Test the file path private attribute"""
        with self.assertRaises(AttributeError):
            self.oO.__objects


if __name__ == "__main__":
    unittest.main()
