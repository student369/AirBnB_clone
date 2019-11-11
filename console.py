#!/usr/bin/python3
"""HBNB Console for AirBnB clone

This is a console to manage some basic commands
To the Airbnb clone project.
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from functools import wraps


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = "(hbnb) "
    __valid_classes = {
        "BaseModel": BaseModel,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """End of File command to quit the program"""
        return True

    def emptyline(self):
        """An empty line and ENTER should not execute anything"""
        pass

    def do_create(self, args):
        """Creates new instance of BaseModel and prints id"""
        v1 = args.split()
        if len(v1) == 0:
            print("** class name missing **")
        else:
            if v1[0] not in self.__valid_classes.keys():
                print("** class doesn't exist **")
            else:
                obj = self.__valid_classes[v1[0]]()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        """Returns the list of an object given"""
        v1 = args.split()
        if len(v1) == 0:
            print("** class name missing **")
        else:
            if v1[0] not in self.__valid_classes.keys():
                print("** class doesn't exist **")
            else:
                try:
                    cl_id = v1[1]
                    storage.reload()
                    objs = storage.all()
                    cl_id = "{:s}.{:s}".format(v1[0], cl_id)
                    if cl_id not in objs.keys():
                        print("** no instance found **")
                    else:
                        print(objs[cl_id])
                except IndexError:
                    print("** instance id missing **")

    def do_destroy(self, args):
        """Returns the list of an object given"""
        v1 = args.split()
        if len(v1) == 0:
            print("** class name missing **")
        else:
            if v1[0] not in self.__valid_classes.keys():
                print("** class doesn't exist **")
            else:
                try:
                    cl_id = v1[1]
                    storage.reload()
                    objs = storage.all()
                    cl_id = "{:s}.{:s}".format(v1[0], cl_id)
                    if cl_id not in objs.keys():
                        print("** no instance found **")
                    else:
                        del objs[cl_id]
                        storage.save()
                except IndexError:
                    print("** instance id missing **")

    def do_update(self, args):
        """Returns the reference of the object updated"""
        v1 = args.split()
        if len(v1) == 0:
            print("** class name missing **")
        else:
            if v1[0] not in self.__valid_classes.keys():
                print("** class doesn't exist **")
            else:
                try:
                    cl_id = v1[1]
                    storage.reload()
                    objs = storage.all()
                    cl_id = "{:s}.{:s}".format(v1[0], cl_id)
                    if cl_id not in objs.keys():
                        print("** no instance found **")
                    else:
                        if len(v1) == 2:
                            print("** attribute name missing **")
                        elif len(v1) == 3:
                            print("** value missing **")
                        elif len(v1) >= 4:
                            attr = v1[2]
                            val = v1[3]
                            setattr(objs[cl_id], attr, val)
                            storage.save()
                except IndexError:
                    print("** instance id missing **")

    def do_all(self, args):
        """Returns the list of objects"""
        v1 = args.split()
        storage.reload()
        actual = storage.all()
        try:
            if v1[0] not in self.__valid_classes.keys():
                print("** class doesn't exist **")
            else:
                cls_name = v1[0]
                l = []
                cls_name = "{:s}.".format(cls_name)
                for k, v in actual.items():
                        if cls_name in k:
                            print(
                                '["' +
                                str(actual[k]) +
                                '"]'
                            )
        except IndexError:
            print(actual)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
