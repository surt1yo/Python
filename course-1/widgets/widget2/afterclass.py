# Write a Python program to create an application to 
# take the date of birth (date, month, and year) as 
# input from the user and return the 
# present age using the Python Tkinter library.
from tkinter import *
from datetime import date
from tkinter import messagebox
# Create the main window
window = Tk()
window.title("Age Calculator")
window.geometry("400x300")

def calculate_age():
    day = int(entry_day.get())
    month = int(entry_month.get())
    year = int(entry_year.get())
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    print(age)
    messagebox.showinfo("Age Result", f"You are {age} years old.")

# Labels and Entry widgets
lbl_day = Label(window, text = "Day of birth:", font = ("Arial", 14))
lbl_day.pack()
entry_day = Entry(window, font = ("Arial", 14))
entry_day.pack()
lbl_month = Label(window, text = "Month of birth:", font = ("Arial", 14))
lbl_month.pack()
entry_month = Entry(window, font = ("Arial", 14))
entry_month.pack()
lbl_year = Label(window, text = "Year of birth:", font = ("Arial", 14))
lbl_year.pack()
entry_year = Entry(window, font = ("Arial", 14))
entry_year.pack()

btn = Button(window, text = "Calculate Age", font = ("Arial", 14), command = calculate_age)
btn.pack(pady = 10)
# Main Loop
window.mainloop()

