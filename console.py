#!/usr/bin/env python3
""" command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Repr the HBNBCommand class """
    prompt = '(hbnb) '
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
