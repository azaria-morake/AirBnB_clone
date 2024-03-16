#!/usr/bin/python3

import json
import cmd

""" This is the control console of the project. """
""" It inherits the cmd modules properties and methods. """

""" Define class. """
class HBNBCommand(cmd.Cmd):
	""" Initialize the attributes. """
	prompt = "\n(hbnb)" + " "
	intro = "\nWelcome to the hbnb console. Type 'help' for available commands. Hit 'Ctrl + D'/'Meta + D' to exit the console."
	
	""" Global attributes """
	
	#usernames = []
	#self.load.usernames() #persist load usernames when session loads again

	""" Initialize __init__ function. """
#	def __init__(self):

	""" Define methods/cmds """
	def emptyline(self):
		# Called when the user enters an empty line
		print("Please enter a command or type 'help' for assistance.")

	def do_greet(self, person):
		print("\nPlease enter your username.\n")
		person = input()
		#user1 = "Keantjie"
		user2 = "azaria-morake"
		#print("Please enter your username.")
		if person == "Keantjie":
			print("\nHello, Keantjie. Welcome to the control console. Type 'help' to see available commands.")
		elif person == user2: #"azaria-morake":
			print("\nHello, azaria-morake. Welcome to the control console. Type 'help' to see available commands.")
		else:
			print("\nHello, Stranger. Welcome to the control console. Type 'help' to see available commands.")
	def do_EOF(self, arg):
		print("Logging off...\n")
		return True
	
	def do_quit(self, arg):
		print("Signing off...\n")
		return True

	def do_authors(self, arg):
		"""\nDisplays the console author's github names. """
		print("\nazaria-morake@github.com\n\nKeantjie@github.com")
	def default(self, line):
		print("\nCommand not recognized. Type 'help' to view all the available commands.")
	def help_greet(self):
		print("\nThis command prompts the console user to enter their username name for a personal welcome message.")

	def preloop(self):
		print("\nThe HBNB project subclasses the cmd module to control the environment.")
		print("\nIt also separates it so that it is genuinley focused on the tasks that need to be completed for the project.")
		print("\n\nThis console is pretty much still under construction and it is basically just the CLI without a GUI.")
		print("\n\n\n============================================================================================================")
		

	""" Here, new objects can be created. """
	def do_create_user(self, arg):
		name = input("Enter first name/s: \n")
		surname = input("\nEnter surname: ")
		username_objects = { "name" : name, "surname" : surname } #create a tuple
		self.usernames.append(username_objects) #add to username data base.

	""" Acces to objects that have been created. """
	def do_username_database(self, arg):
		print("\n".join(str(user) for user in self.usernames))
		#print("\n".str(self.usernames))

if __name__ == '__main__':
	HBNBCommand().cmdloop()
