#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module BaseModel

This module contains the BaseModel class

"""
import datetime as d
import uuid
import models.engine.file_storage as FileStorage


class BaseModel(object):
    """BaseModel class

    A simple empty BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """Returns a BaseModel object"""
        self.storage = FileStorage()
        self.storage.reload()
        if kwargs is not None and len(kwargs) > 0:
            for i, arg in kwargs.items():
                if i == "__class__":
                    arg = self.__class__
                if i == "created_at":
                    arg = d.datetime.strptime(
                        arg, "%Y-%m-%d %H:%M:%S.%f"
                    )
                if i == "updated_at":
                    arg = d.datetime.strptime(
                        arg, "%Y-%m-%d %H:%M:%S.%f"
                    )
                setattr(self, i, arg)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = d.datetime.now()
            self.updated_at = d.datetime.now()

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
        import models.engine.file_storage as storage
        self.updated_at = d.datetime.now()

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
