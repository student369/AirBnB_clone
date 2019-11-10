#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module BaseModel
This module contains the BaseModel class
"""
import models
import datetime as d
from uuid import uuid4


class BaseModel(object):
    """BaseModel class
    A simple empty BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """Returns a BaseModel object"""
        if kwargs is not None and len(kwargs) > 0:
            for i, arg in kwargs.items():
                if i == "__class__":
                    arg = self.__class__
                if i == "created_at":
                    arg = d.datetime.strptime(
                        arg, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                if i == "updated_at":
                    arg = d.datetime.strptime(
                        arg, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                setattr(self, i, arg)
        else:
            self.id = str(uuid4())
            self.created_at = d.datetime.now()
            self.updated_at = d.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns this object in a string format"""
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
        self.updated_at = d.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of this object"""
        dic = self.__dict__.copy()
        dic.__setitem__("__class__", self.__class__.__name__)
        dic.__setitem__(
            "updated_at",
            self.updated_at.isoformat()
        )
        dic.__setitem__("id", self.id)
        dic.__setitem__(
            "created_at",
            self.created_at.isoformat()
        )
        # return (copy.deepcopy(self.__dict__))
        return (dic)
