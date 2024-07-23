#!/usr/bin/python3
"Custom HBNBCommand class"

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        "Method to return nothing if an empty line is entered"
        return

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        return True

    def do_EOF(self):
        "Exit command program with a new line"
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
