#!/usr/bin/env python3
""" command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Repr the HBNBCommand class """
    prompt = '(hbnb) '
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amnenity",
        "Place",
        "Review"
    ]

    def do_create(self, line):
        """ Creates an new instance """
        line_split = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist")
        else:
            print(eval(line_split[0])().id)
            storage.save()
    def do_show(self, line):
        """ Prints the string repr of an instance based on the class name and id """
        line_split = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line_split) == 1:
            print("** instance id is missing **")
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
            print("** class doesn;t exist **")
        elif len(line_split) == 1:
            print("** instance id missing **")
        else:
            try:
                objects = storage.all()
                del objects["{}.{}".format(line_split[0], line_split[1])]
                storage.save()
            except KeyError:
                print(" ** no instance found **")

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
            print("**class doesn't exist **")
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
