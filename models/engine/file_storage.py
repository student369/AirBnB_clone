#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module file_storage

This module contains the FileStorage class

"""
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage(object):
    """FileStorage class

    A simple FileStorage class

    Arguments:
        file_path (str): path to the JSON
        objects (dict): to save the models
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Returns the object dict"""
        return (self.__objects)

    def new(self, obj):
        """Returns nothing

        Set the specific object in the dictionary
        """
        od = self.__objects
        oname = obj.__class__.__name__
        od["{:s}.{:s}".format(oname, obj.id)] = obj

    def save(self):
        """Return nothing

        Save a JSON representation of the object in a file
        """
        filename = self.__file_path
        od = dict()
        list_objs = self.__objects
        for o in list_objs:
            od[o] = list_objs[o].to_dict()
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(od))

    def reload(self):
        """Returns an object from a JSON string

        from the JSON string in an textfile.
        """
        filename = self.__file_path
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                jo = json.loads(f.read())
            for o in jo:
                if o.split(".")[0] == "Place":
                    self.__objects[o] = Place(**(jo[o]))
                elif o.split(".")[0] == "State":
                    self.__objects[o] = State(**(jo[o]))
                elif o.split(".")[0] == "City":
                    self.__objects[o] = City(**(jo[o]))
                elif o.split(".")[0] == "Amenity":
                    self.__objects[o] = Amenity(**(jo[o]))
                elif o.split(".")[0] == "Review":
                    self.__objects[o] = Review(**(jo[o]))
                else:
                    self.__objects[o] = BaseModel(**(jo[o]))
        except IOError:
            return
