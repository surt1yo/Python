# Write a Python program to create an application 
# that takes a length in inches as input from 
# the user and returns the value of that 
# length in centimeters using the Python Tkinter library.
from tkinter import *

# Create the main window
window = Tk()
window.geometry("700x500")
window.title("Inches to Centimeters Converter")

def convert():
    inches = float(entry_inches.get())
    centimeters = inches * 2.54
    textbox.delete("1.0", END)
    textbox.insert(END, f"{inches} inches is equal to {centimeters} centimeters.\n")

# Labels
lbl_inches = Label(window, text = "Enter length in inches:", font = ("Arial", 14))
lbl_inches.pack(pady = 10)
entry_inches = Entry(window, font = ("Arial", 14))
entry_inches.pack(pady = 5)
textbox = Text(window, height = 5, width = 50, font = ("Arial", 14))
textbox.pack(pady = 5)


btn = Button(window, text = "Convert", font = ("Arial", 14), command = convert)
btn.pack(pady = 10)
# Main loop
window.mainloop()