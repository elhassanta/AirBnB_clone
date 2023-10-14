#!/usr/bin/python3
"""
this is the console to execut the commands
"""
import cmd
import json
import re
from models.base_model import BaseModl


class HBNBCommand(cmd.Cmd):
    """
    The class to make the console
    """
    prompt = "(hbnb) "

    def default(self, line):
        """
        overwrite the method default
        """
        print('this is the default method')

    def do_EOF(self, line):
        """
        Handles the end of the file character.
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        If the line is empty do nothing
        """
        pass

    def do_all(self, line):
        """
        Shows the string representation of all objects existing
        """
        print("the all command")

    def do_update(self, line):
        """
        updates an instance
        """
        print("the update command: " + line)

    def do_count(self, line):
        """
        counts the number of instances
        """
        print("the count command: " + line)

    def do_create(self, line):
        """
        Creates a new instance
        """
        print("the create command: " + line)

    def do_destroy(self, line):
        """
        Destroy an exist instance
        """
        print("the destroy command: " + line)

    def do_show(self, line):
        """
        Shows the the representation of an instance
        """
        print("the display command: " + line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
