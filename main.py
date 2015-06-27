# !/usr/bin/python
#
# **********
#
# Programmer: Matthew Griffin
#
# **********
#
# IDEA: A magic 8-ball program that randomly chooses a phrase after
# the user asks a yes/no question
#
# **********
#
# Importing stuff
import time # Making the pause effect
import random # For getting the random results
import sys # For exiting the program
from Tkinter import * # For creating the GUI, imports everything

list = ["Definitly", "Maybe", "Ask a friend", "Definitly...Not!", "Try Again"] # The list of random phrases that can be used
window = Tk() # Creating the window variable

# The window class - this function creates the window, and is called first; It is the class that handles the boring stuff
def Window():
	window.geometry("400x400+200+200") # Setting the size and position of the window
	window.title("8Ball Program") # Setting the title of the window

	Main() # Calls the main function, this will handle all the logic in the window

# The main actions - this function does basiclly all the logic
def Main():

	# Creating the 'Welcome' label
	welcome = Label(window, text = "Welcome to the 8Ball program!")
	welcome.grid(row = 0, column = 0)

	# Creating the 'Enter question' label
	EnterQuest = Label(window, text = "Enter a question: ")
	EnterQuest.grid(row = 1, column = 0)

	# Creating the Entry box
	EntryBox = Entry()
	EntryBox.grid(row  = 2, column = 0)

	# Creating the 'Enter' button
	Enter = Button(window, text = "Enter", command = Logic)
	Enter.grid(row = 2, column = 1)

# This is the logic function - this function is called when the 'Enter' button is pressed	
def Logic():
	time.sleep(3) # Creates a 'Thinking...' effect
	FinalAnswer = Label(window, text = random.choice(list)).grid(row = 4, column = 0) # Displays the final answer to the GUI

Window() # Calls the 'Window()' function
window.mainloop() # Constanly updates the window
