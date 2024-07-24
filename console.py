#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""Module contains a
Custom HBNBCommand class for managing Object Storage
at
"""

from cmd import Cmd


class HBNBCommand(Cmd):
    """Responsible for mapping command to function calls
    and passing arguments to those funtions
    """
    prompt = "(hbnb) "

    def emptyline(self):
        "Method to return nothing if an empty line is entered"
        pass

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        return True

    def do_EOF(self, arg):
        "Exit command program with a new line"
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
