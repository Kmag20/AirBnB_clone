#!/usr/bin/env python3
""" command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from shlex import split
import re


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ Repr the HBNBCommand class """
    prompt = '(hbnb) '
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_create(self, line):
        """ Creates an new instance """
        line_split = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(line_split[0])().id)
            storage.save()
    def do_show(self, line):
        """ Prints the string repr
        of an instance based on the class name and id """
        line_split = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line_split) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            try:
                print(objects["{}.{}".format(line_split[0], line_split[1])])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        line_split = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line_split) == 1:
            print("** instance id missing **")
        else:
            try:
                objects = storage.all()
                del objects["{}.{}".format(line_split[0], line_split[1])]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        line_split = line.split(" ")
        objects = storage.all()
        if line == "":
            for valobj in objects.values():
                print(valobj)
        elif line_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for valobj in objects.values():
                if valobj.__class__.__name__ == line_split[0]:
                    print(valobj)

    def do_update(self, line):
        """ Updates an instance based on the class namee and id by adding or updating """
        objects = storage.all()
        line_split = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line_split) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(line_split[0], line_split[1]) not in objects:
            print("** no instance found **")
        elif len(line_split) == 2:
            print("** attribute name missing **")
        elif len(line_split) == 3:
            print("** value missing **")
        else:
            for object, value in objects.items():
                if "{}.{}".format(line_split[0], line_split[1]) == object:
                    value.__setattr__(line_split[2], line_split[3])
                    storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ command to exit the program """
        print()
        return True

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass

    def help_help(self):
        """ print help command description """
        print("Provides description of a given command")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
