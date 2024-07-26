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
            print(Err1)
        except NameError:  # This implies that our code attempted to ->
            print(Err2)  # -> call eval returned Name()
        else:  # No error thrown, object created!
            print(new_obj.id)  # Printing the object
            new_obj.save()  # calling obj.save, which calls storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance, based
        on the class name, and it id.

        Args:
            arg: string: containing class name and id, both separed by space
        """
        key_object = get_object_by_id(arg)  # Getting key and Object
        # Prevent  Printing None
        if key_object is not None:
            # Extract obj ref, from returned tuple
            print(key_object[1])  #: prints obj str, using __Str__

    def do_destroy(self, arg):
        """Destroys an instance, based
        on the class name, and it id.

        Args:
            arg: string: Expects a class name, with id both seperated by space
        """
        key_object = get_object_by_id(arg)  # Getting key and Object
        # Preventing KeyError Exception
        if key_object is not None:
            all_object = storage.all()  # Getting reference to dict of objs
            del all_object[key_object[0]]  # Index 0 holds the key
            storage.save()

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


def get_object_by_id(arg):
    """Get reference to an instance, based
    on the class name, and it id.

    Args:
        arg: string: containing class name and UUID, both separed by space

    Return: Key with Reference/address to the object else None if not found
    """
    ids = split(arg)  #: list: contains class_name, UUID, or more
    length = len(ids)  #: int: number of args
    if length == 0:
        print(Err1)
    else:  # since there is either classname and/or id
        try:
            klass = eval(ids[0])  #: getting class variable
        except SyntaxError:  #: since the returned value was a number 'id'
            # although this might not be expected to be handled this way
            print(Err1)
        except NameError:
            print(Err2)
        else:  #: So the class exist!
            if length < 2:
                print(Err3)
            else:
                #  Get the key -> <class.id>
                key = ".".join(ids[:2])  # Joining only name and UUID
                try:
                    objects = storage.all()  # Ref to all reloaded obj
                    found_object = objects[key]
                except KeyError:
                    print(Err4)
                else:  # Returning key, and reference to objects
                    return (key, found_object)
    return None  # Explicitly, for clarity sake

# ------- Error Messages ------------ #
Err1 = "** class name  missing **"  #: str: Class name error
Err2 = "** class doesn't exist **"  #: str: Class definition error
Err3 = "** instance id missing **"  #: str: Instance Id error
Err4 = "** no instance found **"    #: str: Instance Not Found error


if __name__ == "__main__":
    HBNBCommand().cmdloop()
