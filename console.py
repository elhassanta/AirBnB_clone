#!/usr/bin/env python3
"""
this is the console to execut the commands
"""
import cmd
import json


class Prompt(cmd.Cmd):
    """
    The class to make the console
    """
    prompt = "(hbnb) "

    def default(self, line):
        """
        overwrite the method default
        """
        pass

    def do_EOF(self, line):
        """
        Handles the end of the file character.
        """
        return True

    def do_quit(self, line):
        """
        Handles the command quit to exit
        """
        return True

    def emptyline(self):
        """
        If the line is empty do nothing
        """
        pass


if __name__ == "__main__":
    Prompt().cmdloop()
