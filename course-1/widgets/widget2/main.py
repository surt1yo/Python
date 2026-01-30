# Create a visual number pad interface using Tkinter! 
# Students will learn to use nested loops, grid layout management, 
# frames, and labels to build a phone-style number 
# pad with organized rows and columns.
from tkinter import *

# Create the main window
window = Tk()
window.title("Number Pad")
window.geometry("300x400")

# Numbers on the Keypad
numbers = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

for i in range(4):
    window.rowconfigure(i, weight=1, minsize = 75)
    window.columnconfigure(i, weight=1, minsize = 50)
    for j in range(3):
        frame = Frame(window, borderwidth = 1, relief = SUNKEN)
        frame.grid(row = i, column = j, sticky="nsew")
        lbl = Label(frame, text = numbers[i][j], font = ("Arial", 24), bg = "lightgray")
        lbl.pack(padx = 3, pady = 3)
window.mainloop()        