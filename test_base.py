#!/usr/bin/python3
"""Unittest for Base class"""
import models.base as b
import pep8
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Base class tests"""

    def test_pep8(self):
        """test the pep8 in the files"""
        p8 = pep8.StyleGuide(quiet=True)
        ret = p8.check_files(
            ['models/base.py',
             'models/rectangle.py',
             'models/square.py',
             'tests/test_models/test_base.py',
             'tests/test_models/test_rectangle.py',
             'tests/test_models/test_square.py']
        )
        self.assertEqual(
            ret.total_errors, 0,
            "Pep 8 errors")

    def test_module_doc(self):
        """A test of module doc"""
        self.assertTrue(len(b.__doc__) > 10)

    def test_class_doc(self):
        """A test of class doc"""
        self.assertTrue(len(Base.__doc__) > 10)

    def test_init_doc(self):
        """A test of constructor doc"""
        self.assertTrue(len(Base.__init__.__doc__) > 10)

    def test_json_string_doc(self):
        """A test of to_json_string function doc"""
        self.assertTrue(
            len(Base.to_json_string.__doc__) > 10
        )

    def test_save_to_file_doc(self):
        """A test of save_to_file function doc"""
        self.assertTrue(
            len(Base.save_to_file.__doc__) > 10
        )

    def test_from_json_string_doc(self):
        """A test of from_json_string function doc"""
        self.assertTrue(
            len(Base.from_json_string.__doc__) > 10
        )

    def test_base_id0(self):
        """Test the correct id of instance"""
        o = Base()
        self.assertEqual(o.id, 1)

    def test_base_id1(self):
        """Test the correct id of instance"""
        o = Base()
        self.assertEqual(o.id, 2)

    def test_base_id2(self):
        """Test the correct id of instance"""
        o = Base()
        self.assertEqual(o.id, 3)

    def test_base_id3(self):
        """Test the correct id of instance"""
        o = Base(12)
        self.assertEqual(o.id, 12)

    def test_base_id4(self):
        """Test the correct id of instance"""
        o = Base()
        self.assertEqual(o.id, 4)

    def test_base_id5(self):
        """Test the correct id of instance"""
        o = Base(89)
        self.assertEqual(o.id, 89)

    def test_json_string0(self):
        """Test if exist the to_json_strin function"""
        self.assertTrue(Base.to_json_string(None))

    def test_json_string1(self):
        """Test if exist the to_json_string function"""
        self.assertTrue(Base.to_json_string([]))

    def test_json_string2(self):
        """Test if exist the to_json_string function"""
        self.assertTrue(
            Base.to_json_string([{'id': 12}])
        )

    def test_json_string3(self):
        """Test if the to_json_string function
        retuns an string
        """
        self.assertIsInstance(
            Base.to_json_string([{'id': 12}]),
            str
        )

    def test_json_from_json0(self):
        """Test if the from_json_strin function
        retuns a empty list
        """
        self.assertEqual(
            Base.from_json_string(None),
            []
        )

    def test_json_from_json1(self):
        """Test if the from_json_strin function
        retuns a empty list
        """
        self.assertEqual(
            Base.from_json_string("[]"),
            []
        )

    def test_json_from_json2(self):
        """Test if the from_json_strin exist
        with an specific parameter
        """
        self.assertTrue(
            Base.from_json_string('[{"id": 89}]')
        )

    def test_json_from_json3(self):
        """Test if the from_json_strin exist
        with an specific parameter
        """
        self.assertIsInstance(
            Base.from_json_string('[{"id": 89}]'),
            list
        )


if __name__ == "__main__":
    unittest.main()
