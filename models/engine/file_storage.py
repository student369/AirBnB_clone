#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module file_storage

This module contains the FileStorage class

"""
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
        self.__objects.__setitem__(obj.id, obj.to_dict())

    def save(self):
        """Return nothing

        Save a JSON representation of the object in a file
        """
        filename = self.__file_path
        list_objs = self.__objects
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(list_objs))

    def reload(self):
        """Returns an object from a JSON string

        A function that get the Python object
        from the JSON string in an textfile.
        """
        filename = self.__file_path
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                pass
        except IOError:
            return (dict())
        with open(filename, mode="r", encoding="utf-8") as f:
            return (json.loads(f.read()))
