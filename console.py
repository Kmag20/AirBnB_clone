#!/usr/bin/env python3
""" command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Repr the HBNBCommand class """
    prompt = '(hbnb) '
    def do_quit(self, line):
        """ command to exit the program """
        return True

    def do_EOF(self, line):
        """ command to exit the program """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
