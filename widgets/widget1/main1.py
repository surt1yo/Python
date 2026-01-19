# Create an interactive GUI application using Tkinter 
# that greets users by name and displays today's date! 
# Students will learn to build windows, add widgets, handle 
# button clicks, and display dynamic messages in a text box.
from tkinter import *
from datetime import date
# Create the main window
window = Tk()
window.title("Greet people")
window.geometry("400x300")
def Greet():
    name=nameentry.get()
    msg="Welcome to the application"+"\n"
    greeting="Hello "+name+"\n"
    date_msg="Today's date is: "+str(date.today())
    textbox.insert(END, msg)
    textbox.insert(END, greeting)
    textbox.insert(END, date_msg)
lbl = Label(window, text="Welcome to my first GUI!", font=("Arial", 12, "bold"), fg="blue", bg="yellow", height=1, width=300)
lbl.pack()
namelabel = Label(window, text="Enter your name:")
namelabel.pack()
nameentry = Entry()
nameentry.pack()
textbox = Text(window, height=4, width=40)
textbox.pack()
btn = Button(window, text="Submit", height=1 , width=10, bg="blue", fg="white", command=Greet)
btn.pack()

# Keep the window open
window.mainloop()