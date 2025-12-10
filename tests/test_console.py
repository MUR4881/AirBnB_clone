from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
# -*- encoding: utf-8 -*-

""" Implementing test for the console:
    The console is useful for creating and
    destroying objects, which is used for development
    and for the backend management of the Airbnb clone project

    # The TestConsole, side  loads tests during instiation!

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


def createTest(self):
    '''Executes an assertion, each time it is called, by taking
    advantage of eval and the class attributes (`lists` of lists/lines
    and line_count that has been set to zero, in the class)
    '''

    line = self.__class__.line_count  #: just to keep the lines below shorter

    # Ensuring incrementation, which might not happen due to of assertion error
    # thereby putting the incrementation before the assertion
    self.__class__.line_count += 1  #: coincidentally biasing for the index 0

    # |----- An example of one of the lists in the list self.lines
    # |      That was generated in the test class from the test file
    # V
    # ['assertGreater', 'count Place', 52, <console output for count place>]
    # line + 1 represents the actual line in the file which is index + 1
    eval(f"self.{self.lines[line][0]}")(self.lines[line][3],
                                        self.lines[line][2],
                                        f"@ line: {line+1}"
                                        )


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
        cls.skipTest(True, "Skipping, this testClass is only a sacrifice")


class TestConsole(TestCaseEscape):
    '''Testing the  Console
    Algorithm:
        1: Setup interception for any output(from the console) to stdout
        2: Open & read a line from the testfile (.ftst):
            assertion_Type#console command#expected/compared output
        3: Refine and split the line into columns
            e.g ['assertRegex', 'create Place', '[0-9A-Z]*']
        4: Execute the 2nd column index 1, with the cmd
            HBNBCommand().onecmd(line[1])
        5: Intercept, clean, extract the most recent output from the console
            out = output.getValue().strip("\n").split("\n")[-1]
        6: Append the console output to the list/line (not lines!)
            line.append(out)
        7:  Convert integer strings to integer where and when necessery
                if line[0] in ['assertLess', 'assertGreater', 'assertEqual']:
                    line[3] = int(line[3])  #: The console output
                    line[2] = int(line[2])  #: The expected/toBeCompared output

        8: Check if the Current line references any of the prevs cmd outputs
        then put it in place.
            it references by putting -n in the third column - the place meant
            for the expected/toBeCompared output. where n represents the index
            from the last e.g -1 -> present, -2 -> prev, -3 ->  prev prev
            if line[2] > 0:
                line[2] = lines[line[2]][2]

        9: Append the new line/list to the overall record of lines
                lines.append(line)
        10: Now set a "test_n" attribute to a lamda function that calls
        createTests
                Go find out more about createTest in the test function
        11: Increment the line_count

    '''

    @classmethod
    def setUpClass(cls):
        '''Overriding the previous SetUp from the previous class
        '''
        pass

    with patch("sys.stdout", new=StringIO()) as output:
        with open(__File__, "r") as file:
            line_count = 0  #: Keeping track of line number for file
            lines = []  #: To store the refined and grouped lines of the file

            #: Generating tests begin here
            #  Read line from file
            for line in file.readlines():
                #: Removing the newline character
                line = line[:-1]
                #: Separate Columns in the line
                line = line.split("#")
                #: Execute the second column with the console/cmd
                HBNBCommand().onecmd(line[1])
                #: Clean the console output(s) & split them. but why?
                #  Ans: Well, that was one of the bugs, everytime we
                #  try getting the console output, this method {getvalue()}
                #  returns all the previous output from the console to.
                #  therefore we split and take the last of the list which
                #  represent the present output of the console.
                out = output.getvalue().strip("\n").split("\n")
                # append the console output to the line -> the list of lists
                # that contains all the rows and columns from the testfile
                line.append(out[-1])

                #  now convert to integer where necessary and if necessary
                if line[0] in ['assertLess', 'assertGreater', 'assertEqual']:
                    line[3] = int(line[3])
                    line[2] = int(line[2])

                #  check if the current, requires any of the previous
                #  console output to run, which is indicated with negative
                #  integer @ the last column meant for the expected output
                if isinstance(line[2], int) and line[2] < 0:
                    #  summary: indexing the lines with the specified index
                    #  in the 3rd column of the present line, then indexing
                    # the 4th column, for the console output of that line.
                    line[2] = lines[line[2]][3]
                # Add the newly purified and cleaned line to the
                # list of lists/lines
                lines.append(line)
                # Now set an attribute(a method) called test_n where
                # n is the line number in the test file, and set it to a lambda
                # function that call the function `createTest`, that reffrences
                # the attributes (e.g lists, line_count) and makes an assertion
                # taking advantage of eval
                setattr(TestCaseEscape, f"test_{line_count+1}",
                        lambda self: createTest(self))
                # increment line count, so test_n  name is always different.
                line_count += 1  #: keeping count of current line in file

    # Resetting the line_count attribute list index to zero, so 'test_n' calls
    # can index with it as a class attr from zero of the list of lists, whose
    # length it represents.
    line_count = 0
