#!/usr/bin/python3

import json
import cmd

""" This is the control console of the project. """
""" It inherits the cmd modules properties and methods. """

""" Define class. """

class HBNBCommand(cmd.Cmd):
	""" Initialize the attributes. """
	prompt = "(hbnb) "
	
	""" Define methods/cmds """
	
	def do_quit(self, arg):
		print("Logging off...\n")
		return True
	
	def do_EOF(self, arg):
		return True
	""" help_quit: provides help information for the command quit."""
	def help_quit(self):
		print("\nThis command exits the console.")

	def help_EOF(self):
		print("\nThis command exits the console.")

if __name__ == '__main__':
	HBNBCommand().cmdloop()
