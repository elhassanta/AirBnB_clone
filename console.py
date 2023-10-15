#!/usr/bin/python3
"""
this is the console to execut the commands
"""
import cmd
import sys
import json
import re
from models.base_model import BaseModel
from shlex import split
from models import storage


def parse(line):
    """
    this function used to parse a command
    """
    cur_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)
    if cur_braces is None:
        if brackets is None:
            return [i.strip(",") for i in line]
        else:
            lexer = split(line[:brackets.span()[0]])
            c_cmd = [i.strip(",") for i in lexer]
            c_cmd.append(brackets.group())
            return c_cmd
    else:
        lexer = split(line[:cur_braces.span()[0]])
        print(lexer)
        c_cmd = [i.strip(",") for i in lexer]
        c_cmd.append(cur_braces.group())
        return c_cmd


class HBNBCommand(cmd.Cmd):
    """
    The class to make the console
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "State",
            "City",
            "Place",
            "User",
            "Review",
            "Amenity",
    }

    def default(self, line):
        """
        overwrite the method default
        """
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }
        match = re.search(r"\.", line)
        if match is not None:
            l_line = [line[:match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", l_line[1])
            if match is not None:
                command = [l_line[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(l_line[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unkown syntax: {}".format(line))
        return False

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
        l_line = parse(line)
        print(l_line)
        obj_dict = storage.all()
        if len(l_line) == 0:
            print("** class name missing **")
        elif l_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(l_line) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l_line[0], l_line[1]) not in  obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(l_line[0], l_line[1])])
        print("the create command: " + line)

    def do_destroy(self, line):
        """
        Destroy an exist instance
        """
        l_line = parse(line)
        print("the destroy command: " + line)

    def do_show(self, line):
        """
        Shows the the representation of an instance
        """
        print("the display command: " + line)


if __name__ == "__main__":
    if sys.stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        HBNBCommand().cmdloop()
        print()
