from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
# -*- encoding: utf-8 -*-

""" Implementing test for the console:
    The console is useful for creating and
    destroying objects, which is used for development
    and for the backend management of the Airbnb clone project

    Functionalities/Commands to test for:
    * ```quit``` and EOF to the exit the program
    * ```help``` (this action is provided by default by cmd but you
    should keep it updated and documeted as you work through
    tasks)
    * a custom prompt: (hbnb)
    * an ```empty line + ENTER``` shouldn't execute anything

    * ```create```: Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id. Ex: $ create BaseModel

        If the class name is missing,
            print ** class name missing ** (ex: $ create)

        If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ create MyModel)

    * ```show```: Prints the string representation of an instance based
            on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

        If the class name is missing,
            print ** class name missing ** (ex: $ show)

        If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ show MyModel)

        If the id is missing,
            print ** instance id missing ** (ex: $ show BaseModel)

        If the instance of the class name doesn’t exist for the id,
            print ** no instance found ** (ex: $ show BaseModel 121212)

    * ```destroy```: Deletes an instance based on the class name and id
                (save the change into the JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234.

         If the class name is missing,
            print ** class name missing ** (ex: $ destroy)

        If the class name doesn’t exist,
            print ** class doesn't exist ** (ex:$ destroy MyModel)

        If the id is missing,
            print ** instance id missing ** (ex: $ destroy BaseModel)

        If the instance of the class name doesn’t exist for the id,
            print ** no instance found ** (ex: $ destroy BaseModel 121212)

    * ```all```: Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)

        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ all MyModel)

    * ```update```: Updates an instance based on the class name
                    and id by adding or updating attribute
                    (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Usage: update <class name> <id> <attribute name> "<attribute value>"
            * Only one attribute can be updated at the time
            * You can assume the attribute name is valid
            (exists for this model)
            * The attribute value must be casted to the attribute type

            If the class name is missing,
                print ** class name missing ** (ex: $ update)

            If the class name doesn’t exist,
                print ** class doesn't exist ** (ex: $ update MyModel)
            If the id is missing,
                print ** instance id missing **(ex: $ update BaseModedl)

            If the instance of the class name doesn’t exist for the id,
                print ** no instance found ** (ex: $ update BaseModel 121212)

            If the attribute name is missing,
                print ** attribute name missing **
                (ex: $ update BaseModel existing-id)

            If the value for the attribute name doesn’t exist,
                print ** value missing **
                ex: $ update BaseModel existing-id first_name)

            All other arguments should not be used
            (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
            first_name "Betty" = $
            update BaseModel 1234-1234-1234 email "aibnb@mail.com")
            id, created_at and updated_at cant’ be updated.
            You can assume they won’t be passed in the update command

            Only “simple” arguments can be updated: string, integer and float.
            You can assume nobody will try to update list of ids or datetime


    ### Let’s add some rules:

        * You can assume arguments are always in the right order
        * Each arguments are separated by a space
        * A string argument with a space must be between double quote
        * The error management starts from the first argument to the last one

    ** Update your command interpreter (console.py) to allow those actions:
    show, create, destroy, update and all with all classes created previously.

    ** Update your command interpreter (console.py) to retrieve
    all instances of a class by using: <class name>.all().

    ** Update your command interpreter (console.py) to retrieve an
    instance based on its ID: <class name>.show(<id>).

    Errors management must be the same as previously.

    ** Update your command interpreter (console.py) to destroy an
    instance based on his ID: <class name>.destroy(<id>).

    Errors management must be the same as previously.

    ** Update your command interpreter (console.py) to update an instance
    based on his ID: <class name>.
    update(<id>, <attribute name>, <attribute value>).

    Errors management must be the same as previously.

    ** Update your command interpreter (console.py) to update an instance
    based on his ID with a dictionary: <class name>.
    update(<id>, <dictionary representation>).

    Errors management must be the same as previously.

Enjoy your first console!

"""

# file with the foramt assertions#testinput#expected_output
__File__ = "filetest.ftst"

# def __init__(self, methodName='test_me'):
#    ''' Dynamcally generating test units from
#    a file
#    '''
#    print("wow")

class TestCaseEscape(TestCase):
    '''Preventing, adding the test_ methods to the
    the main TestCase class, which causes the tests
    to be ran for all other TestClasses inheriting
    from TestCase
    '''

    # preventing execution of test_methods that would be set
    # to this class
    @classmethod
    def setUpClass(cls):
        cls.skipTest(True,"Skipping, this testClass is only a sacrifice")


class TestConsole(TestCaseEscape):
    '''Testing the  Console
    '''

    @classmethod
    def setUpClass(cls):
        '''Overriding the previous SetUp from the previous class
        '''
        pass


    with patch("sys.stdout", new=StringIO()) as output:
        with open(__File__, "r") as file:
            line_count = 0  #: Keeping track of line number for file
            for line in file.readlines():
                line = line[:-1]  #: Removing the newline character
                line = line.split("#")
                HBNBCommand().onecmd(line[1])
                line.append(output.getvalue()[:-1])
                setattr(TestCaseEscape, f"test_{line_count}",
                        lambda self: eval(f"self.{TestConsole.line[0]}")\
                        (TestConsole.line[3], TestConsole.line[2],
                        f"@ line: {TestConsole.line_count}"
                        ))
                line_count += 1  #: keeping count of current line in file
