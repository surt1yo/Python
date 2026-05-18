# Write a Python program to create an application that 
# accepts a password from the user and displays its 
# strength based on the length of the password using 
# the Python Tkinter library.
from tkinter import *
import random

def check_strength():
    password = entry.get()
    length = len(password)
    strength_label.config(text="")
    
    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif length <= 12:
        strength = "Strong"
        color = "lightgreen" 
    else:
        strength = "Very Strong"
        color = "darkgreen"  
    
    strength_label.config(text=strength, fg=color)

root = Tk()
root.title("Length Converter App")  
root.geometry("400x400")

title_label = Label(root, text="Password Strength Checker", font=("Arial", 16))
title_label.pack(pady=20)

entry_label = Label(root, text="Enter Password:")
entry_label.pack()

entry = Entry(root, width=30, show="*")
entry.pack(pady=10)
entry.focus_set()

button = Button(root, text="Check Strength", command=check_strength, bg="lightblue")
button.pack(pady=10)

strength_label = Label(root, text="", font=("Arial", 20, "bold"))
strength_label.pack(pady=50)

root.mainloop()
