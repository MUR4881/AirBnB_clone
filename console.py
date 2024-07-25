#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""Module contains a
Custom HBNBCommand class for managing Object Storage
at
"""
# Importing dependencies
from cmd import Cmd
from models.base_model import BaseModel


class HBNBCommand(Cmd):
    """Responsible for mapping command to function calls
    and passing arguments to those funtions
    """
    prompt = "(hbnb) "

    def do_create(self, klass):
        """Create a new instance of a give class
        and saves it to the JSON file

        Args:
            klass: The name of the class as a string
        """
        # create the instance, remember the storage automatically reload
        # Reload, as in read everything stored in the file
        # And reload as been called in __init__.py
        try:
            new_obj = eval(klass)()  #: eval convert the string to the class
        except SyntaxError:  # eval throws syntax error on empty string
            # which means class name wasn't passed
            print("** class name missing **")
        except NameError:  # This implies that our code attempted to ->
            print("** class doesn't exist **")  # -> call eval returned Name()
        else:  # No error thrown, object created!
            print(new_obj.id)  # Printing the object
            new_obj.save()  # calling obj.save, which calls storage.save()

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
