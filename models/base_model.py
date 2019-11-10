#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module BaseModel
This module contains the BaseModel class
"""
import models
from datetime import datetime
import uuid
class BaseModel():
    """BaseModel class
    A simple empty BaseModel class
    """
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) != 0:
            for i, arg in kwargs.items():
                if i == "__class__":
                    arg = self.__class__
                if i == "created_at":
                    arg = datetime.strptime(
                        arg, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                if i == "updated_at":
                    arg = datetime.strptime(
                        arg, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                if i == "my_number":
                    self.my_number = arg
                if i == "name":
                    self.name = arg
                if i == "id":
                    self.id = arg
                setattr(self, i, arg)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    def __str__(self):
        """Oberwrite the __str__ magic method"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                            self.__dict__))
    def save(self):
        """Method to updates the instance"""
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """Returns a dictionary representation of this object"""
        dicver = self.__dict__.copy()
        dicver["__class__"] = self.__class__.__name__
        dicver["updated_at"] = self.__dict__["updated_at"].isoformat()
        dicver["created_at"] = self.__dict__["created_at"].isoformat()
        return (dicver)
