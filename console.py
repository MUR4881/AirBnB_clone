#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""Module contains a
Custom HBNBCommand class for managing Object Storage
at
"""
# Importing dependencies
from cmd import Cmd
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(Cmd):
    """Responsible for mapping command to function calls
    and passing arguments to those funtions
    """
    prompt = "(hbnb) "

    def default(self, line):
        """Handling all <class_name>.command() with default
        Or calling back the original default

        Args:
            line: The line for which command has not been implemented
        """
        args = replace(line).split()
        # swap first two: as in User.create as create User
        klass = args[0]
        args[0] = args[1]
        args[1] = klass

        line = " ".join(args)
        # If command doesn't exist to handle the command
        if f"do_{args[0]}" not in HBNBCommand.__dict__:
            super().default(line)
            return
        # Run the class command
        self.onecmd(line)

    def do_create(self, klass):
        """Create a new instance of a give class
        and saves it to the JSON file

        Args:
            klass: The name of the class as a string
        """
        # No Need to slip_strip args, # (klass) is same as klass; when not str
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

    def do_all(self, klass):
        """Displays String representation of all instances
        based on or not on the class name

        Args:
            klass: The optional class Name
        """
        klass = replace(klass)  # Removing unncessary chars
        str_list = []  # To store list of str
        typ = None
        length = len(klass)
        # Prevent passing empty string to eval()
        if length != 0:
            try:  # Ensure class is defined
                typ = type(eval(klass))  #: catching other type
            except Exception:  # to prevent unneccessary transverse
                print(Err2)
                return  # preventing unneccessary transverse
            finally:  # Survived eval for being a None class variable or int ?
                # klass is defined in scope, but not a class?
                if typ is not type and typ is not None:
                    print(Err2)
                    return

        # made through as a defined class, or class not given
        for key, obj in storage.all().items():  # list of tuples:(key,obj)
            # Ensuring for empty string or fully defined class
            if (length == 0) or (klass in key.split(".")):
                str_list.append(str(obj))

        print(str_list)

    def do_update(self, args):
        """Updates an instance based on it class name and id
        by adding or updating attribute (save the changes into
        the JSON file).

        Args:
            args: contains, class_name, UUID, attribute, value
        """
        key_obj = get_object_by_id(args)  # tuple: of key_and obj
        # is the object None?
        if key_obj is not None:
            args = replace(args).split()  # list: of cmdline args
            length = len(args)  # int: the number arguments
            if length < 3:
                print("** attribute name missing **")
            elif length < 4:
                print("** value missing **")
            else:  # attributes and values are available!
                attribute = args[2]  #: attibute
                value = args[3]
                # Ensure attribute name, starts with alpa
                if attribute[0].isalpha():  # Ensure attr name is appropriate
                    # ensure to cast to the of value giving, str is default
                    if value.isdigit():  # Either float or integers
                        try:
                            value = int(value)
                        except ValueError:  # int() can not handle float str
                            value = float(value)  # float() can handle int str
                    # value casted or not, as long as attribute starts w alpa
                    # key_obj contains tuple of key and obj,! get_obj_by_id()?
                    obj = key_obj[1]  # Object
                    setattr(obj, attribute, value)  # setting attributes
                    storage.save()  # Saving changes to disk also
                else:  # attribute doesn't start with alphabet
                    # which, causes the attribute to be in accessibe
                    # after it has been set. since var can start with digit
                    print("** Attribute name will cause issues **")

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


def replace(arg):
    """removes '.(),'
    by using space as the default separator

    Args:
        arg: The passed arguments to be separated

    Return: A list of the splitted.
    """
    # Replaces Unnecessary characters with space
    reform_arg = ""
    for character in arg:
        if character in ",()\"'.":
            character = " "  # Replacement
        reform_arg += character

    return reform_arg.strip()  # removing spaces added to ends


def get_object_by_id(arg):
    """Get reference to an instance, based
    on the class name, and it id.

    Args:
        arg: string: containing class name and UUID, both separed by space

    Return: Key with Reference/address to the object else None if not found
    """
    ids = replace(arg).split()  #: list: contains class_name, UUID, or more
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
Err1 = "** class name missing **"  #: str: Class name error
Err2 = "** class doesn't exist **"  #: str: Class definition error
Err3 = "** instance id missing **"  #: str: Instance Id error
Err4 = "** no instance found **"    #: str: Instance Not Found error


if __name__ == "__main__":
    HBNBCommand().cmdloop()
