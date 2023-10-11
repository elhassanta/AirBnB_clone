#!/usr/bin/env python3
"""
this is the console to execut the commands
"""
import cmd
import json
import re


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
    def do_all(self, line):
        """
        Shows the string representation of all objects existing
        """
        pass
    
    def do_update(self, line):
        """
        updates an instance
        """
        pass

    def do_count(self, line):
        """
        counts the number of instances
        """
        pass
    
    def do_create(self, line):
        """
        Creates a new instance
        """
        pass
    
    def do_destroy(self, line):
        """
        Destroy an exist instance
        """
        pass

    def do_show(self, line):
        """
        Shows the the representation of an instance
        """
        pass



if __name__ == "__main__":
    Prompt().cmdloop()
