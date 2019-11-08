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
        return (self.__dict__)
