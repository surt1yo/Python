# Create a virus scanner simulation with 
# pop-up alerts using Tkinter! Students 
# will learn to use messagebox to display 
# warning dialogs, understand button commands, 
# and create interactive alert 
# systems for desktop applications.
from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()
window.title("Virus Scanner")
window.geometry("400x200")

def scan():
    messagebox.showwarning("Virus Alert", "A Virus has been detected on your system!")
# Button
btn = Button(window, text = "Scan for Viruses", font = ("Arial", 16), command = scan)
btn.pack(pady = 50)

# Main loop
window.mainloop()