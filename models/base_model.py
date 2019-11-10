#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module BaseModel
This module contains the BaseModel class
"""
import models
from datetime import datetime
import uuid
class BaseModel():
import datetime as d
from uuid import uuid4


class BaseModel(object):
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
<<<<<<< HEAD
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
=======
            self.id = str(uuid4())
            self.created_at = d.datetime.now()
            self.updated_at = d.datetime.now()
            models.storage.new(self)

>>>>>>> 295b18ebb04247a35326e8d197262104f1f39fe0
    def __str__(self):
        """Oberwrite the __str__ magic method"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                            self.__dict__))
    def save(self):
        """Method to updates the instance"""
<<<<<<< HEAD
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """Returns a dictionary representation of this object"""
        dicver = self.__dict__.copy()
        dicver["__class__"] = self.__class__.__name__
        dicver["updated_at"] = self.__dict__["updated_at"].isoformat()
        dicver["created_at"] = self.__dict__["created_at"].isoformat()
        return (dicver)
=======
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
>>>>>>> 295b18ebb04247a35326e8d197262104f1f39fe0
