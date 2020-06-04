# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:43:15 2019

@author: Shreya Jaiswal
"""

import tkinter 
import random

computer_guess = random.randint(1,10)

def check():
	#Get the value from txt_guess
	user_guess = int(txt_guess.get())

	#Determine higher, lower, or just right
	if user_guess < computer_guess:
		msg = "Higher!"
	elif user_guess > computer_guess:
		msg = "Lower!"
	elif user_guess == computer_guess:
		msg = "Correct!"
	else:
		msg = "Something went wrong..."
		
	#Show the result
	lbl_result["text"] = msg
	
	#Clear txt_guess
	txt_guess.delete(0, 5)

def reset():
	#Declare the global variable
	global computer_guess
	#Get a random number
	computer_guess = random.randint(1,10)
	#Change the lbl_result text
	lbl_result["text"] = "Game reset. Guess again!"

#Create root window
root = tkinter.Tk()

#Change root window background color
root.configure(bg="white")

#Change the title
root.title("Guess the number!")

#Change the window size
root.geometry("250x75")

#Create Widgets
lbl_title = tkinter.Label(root, text="Welcome to the Guessing Game!", bg="white") 
lbl_title.pack()

lbl_result = tkinter.Label(root, text="Good Luck!", bg="white") 
lbl_result.pack()

btn_check = tkinter.Button(root, text="Check", fg="green", bg="white", command=check)
btn_check.pack(side="left")

btn_reset = tkinter.Button(root, text="Reset", fg="red", bg="white", command=reset)
btn_reset.pack(side="right")

txt_guess = tkinter.Entry(root, width=3)
txt_guess.pack()

#Start the main events loop
root.mainloop()
root.destroy()