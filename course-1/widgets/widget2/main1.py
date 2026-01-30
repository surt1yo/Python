# Create a user registration form with Tkinter! 
# Students will learn to build a login interface 
# with text input fields, password masking, button 
# functionality, and message display. Perfect for 
# understanding form creation and user 
# interaction in GUI applications.
from tkinter import *

# Create the main window
window = Tk()
window.title("User Registration Form")
window.geometry("500x400")

def Congrats():
    name = entry1.get()
    email = entry2.get()
    password = entry3.get()
    confirm_password = entry4.get()

    # Check for missing inputs
    if not name or not email or not password or not confirm_password:
        textbox.insert(END, "Missing Inputs, please try again\n")
        return
    # Check password match
    if password != confirm_password:
        textbox.insert(END, "Passwords do not match, please try again\n")
        return

    # Check email format
    email_domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    if not any(email.endswith(f"@{domain}") for domain in email_domains):
        textbox.insert(END, "Incorrect email, please try again\n")
        return

    msg = f"Congratulations {name}, your account has been created!\n"
    textbox.insert(END, msg)
    
# Frame
frame = Frame(window, height = 250, width = 350, bg = "lightblue")
frame.place(x = 20, y = 20)

# Labels and Entry widgets
lbl1 = Label(frame, text = "Full name:", bg = "blue", fg = "white")
lbl1.place(x = 10, y = 20)
entry1 = Entry(frame, width = 30)
entry1.place(x = 100, y = 20)

lbl2 = Label(frame, text = "Email:", bg = "blue", fg = "white")
lbl2.place(x = 10, y = 60)
entry2 = Entry(frame, width = 30)
entry2.place(x = 100, y = 60)

lbl3 = Label(master=frame, text = "Password:", bg = "blue", fg = "white")
lbl3.place(x = 10, y = 100)
entry3 = Entry(frame, width = 30, show="*")
entry3.place(x = 100, y = 100)

lbl4 = Label(frame, text = "Confirm Password:", bg = "blue", fg = "white")
lbl4.place(x = 10, y = 140)
entry4 = Entry(frame, width = 30, show="*")
entry4.place(x = 130, y = 140)
# Button
btn = Button(window, text = "Create Account", bg = "blue", fg = "white", command = Congrats )
btn.place(x = 140, y = 200)

textbox = Text(window, bg="#BEBEBE", fg="black")
textbox.place(y = 250)

# Main loop
window.mainloop()