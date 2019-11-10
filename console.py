#!/usr/bin/python3
"""HBNB Console for AirBnB clone

This is a console to manage some basic commands
To the Airbnb clone project.
"""
import cmd
import models
from models import storage
from modes.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = "(hbnb) "

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
            if v1[0] not in valid_classes:
                print("** class doesn't exist **")
            else:
                obj = eval(v1[0])()
                obj.save()
                print(obj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
