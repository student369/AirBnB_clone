#!/usr/bin/python3
"""HBNB Console for AirBnB clone

This is a console to manage some basic commands
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
