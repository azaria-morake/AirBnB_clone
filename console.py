#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_create(self):

    def do_show(self):
        self

    def do_destroy(self):

    def do_all(self):

    def do_update(self):

    def help_EOF(self):
        print("Quit command to exit the program")
    def emptyline(self):
        pass
if __name__ == '__main__':
	HBNBCommand().cmdloop()
