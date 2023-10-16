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
            return [i.strip(",") for i in split(line)]
        else:
            lexer = split(line[:brackets.span()[0]])
            c_cmd = [i.strip(",") for i in lexer]
            c_cmd.append(brackets.group())
            return c_cmd
    else:
        lexer = split(line[:cur_braces.span()[0]])
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
        print()
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
        l_line = parse(line)
        if len(l_line) > 0 and l_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            l_objs = []
            for obj in storage.all().values():
                if len(l_line) > 0 and l_line[0] == obj.__class__.__name__:
                    l_objs.append(obj.__str__())
                elif len(l_line) == 0:
                    l_objs.append(obj.__str__())
            print(l_objs)

    def do_update(self, line):
        """
        updates an instance
        """
        l_line = parse(line)
        obj_dict = storage.all()

        if len(l_line) == 0:
            print("** class name missing **")
            return False
        if l_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if "{}.{}".format(l_line[0], l_line[1]) not in obj_dict:
            print("** no instance found **")
            return False
        if len(l_line) == 2:
            print("** attribute name missing **")
            return False
        if len(l_line) == 3:
            try:
                type(eval(l_line[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(l_line) == 4:
            obj = obj_dict["{}.{}".format(l_line[0], l_line[1])]
            if l_line[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[l_line[3]])
                obj.__dict__[l_line[2]] = valtype(l_line[3])
        elif type(eval(l_line[2])) == dict:
            obj = obj_dict["{}.{}".format(l_line[0], l_line[1])]
            for k, v in eval(l_line[0], l_line[1]).items():
                if (k in obj.__class__.__dic__.keys()
                        and type(obj.__class__.__dict__[k])
                        in {str, float, int}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, line):
        """
        counts the number of instances
        """
        l_line = parse(line)
        count = 0
        obj_list = storage.all().values()
        for obj in obj_list:
            if l_line == obj.__class__.__name__:
                count += 1
        print(count)

    def do_create(self, line):
        """
        Creates a new instance
        """
        l_line = parse(line)
        obj_dict = storage.all()
        if len(l_line) == 0:
            print("** class name missing **")
        elif l_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(l_line[0])().id)
            storage.save()

    def do_destroy(self, line):
        """
        Destroy an exist instance
        """
        l_line = parse(line)
        obj_dict = storage.all()
        if len(l_line) == 0:
            print("** class name missing **")
        elif l_line[0] not in HBNBCommand._classes:
            print("** class doesn't exist **")
        elif len(l_line) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l_line[0], l_line[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(l_line[0], l_line[1])]
            storage.saev()

    def do_show(self, line):
        """
        Shows the the representation of an instance
        """
        l_line = parse(line)
        obj_dict = storage.all()
        if len(l_line) == 0:
            print("** class doesn't exist **")
        elif l_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(l_line) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l_line[0], l_line[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(l_line[0], l_line[1])])


if __name__ == "__main__":
    if sys.stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        print()
