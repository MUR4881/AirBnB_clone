#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""Module contains a
Custom HBNBCommand class for managing Object Storage
at
"""
# Importing dependencies
from cmd import Cmd
from models import storage
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

    def do_show(self, arg):
        """Prints the string representation of an instance, based
        on the class name, and it id.

        Args:
            arg: string: containing class name and id, both separed by space
        """
        args = split(arg)  #: list: list of the args
        length = len(args)  #: int: number of args
        if length == 0:
            print("** class name missing **")
        else:  # since there is either classname and/or id
            try:
                klass = eval(args[0])  #: getting class variable
            except SyntaxError:  #: since the returned value was a number 'id'
                # although this might not be expected to be handled this way
                print("** class name missing **")
            except NameError:
                print("**class doesn't exist **")
            else:  #: So the class exist!
                if length < 2:
                    print("** instance id missing **")
                else:
                    #  Get the key -> <class.id>
                    key = ".".join(args[:2])  # Joining only 1st 2 args as key
                    try:
                        objects = storage.all()  # Ref to all reloaded obj
                        search_object = objects[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        print(search_object)  #: prints obj str, using __Str__

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

# ----- Complementary/Supplementary Functions --------- #


def split(arg):
    """Split arguments into list of args
    by using space as the defaul separator

    Args:
        arg: The passed arguments to be separated

    Return: A list of the splitted.
    """
    return arg.split()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
