#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module BaseModel

This module contains the BaseModel class

"""
import datetime
import uuid


class BaseModel(object):
    """BaseModel class

    A simple empty BaseModel class
    """
    def __init__(self):
        """Returns a BaseModel object"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        """Oberwrite the __str__ magic method"""
        return (
            "[{:s}] ({:s}) {:s}"
            .format(
                str(self.__class__.__name__),
                str(self.id),
                str(self.__dict__)
            )
        )

    def save(self):
        """Method to updates the instance"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """Returns a dictionary representation of this object"""
        dicver = dict()
        dicver.__setitem__("my_number", self.my_number)
        dicver.__setitem__("my_name", self.name)
        dicver.__setitem__("__class__", self.__class__.__name__)
        dicver.__setitem__(
            "updated_at",
            self.updated_at.isoformat(' ')
        )
        dicver.__setitem__("id", self.id)
        dicver.__setitem__(
            "created_at",
            self.created_at.isoformat(' ')
        )
        return (dicver)
