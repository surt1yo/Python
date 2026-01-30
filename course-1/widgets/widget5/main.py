# Create a root window that contains a button. 
# And when the user clicks this button, a new window 
# will open up using the Top Level functionality of Tkinter.
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
# Creating the main window
root = Tk()
root.title("Denomination Calculator")
root.configure(bg="lightblue")
root.geometry("650x400")

# Functions
def show_msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()
    
def topwin():
    top = Toplevel()
    top.title("Denomination Counter")
    top.geometry("600x500")
    top.configure(bg="light yellow")

    def Calculator():
        amount = int(amount_entry.get())
        n2k = amount // 2000
        amount = amount % 2000
        n5h = amount // 500
        amount = amount % 500
        n1h = amount // 100
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t1.insert(0, str(n2k))
        t2.insert(0, str(n5h))
        t3.insert(0, str(n1h))

    lbl = Label(top, text="Enter the Amount:", bg="light yellow")
    lbl.place(x=200,y=50)

    amount_entry=Entry(top)
    amount_entry.place(x=200,y=80)

    btn1 = Button(top, text="Calculate", bg="light green", command=Calculator)
    btn1.place(x=250,y=120)

    lbl1 = Label(top, text="Here are the denominations:", bg="light yellow")
    lbl1.place(x=200,y=200)

    l1 = Label(top, text="2000 Notes: ", bg="light yellow")
    l1.place(x=200,y=230)
    l2 = Label(top, text="500 Notes: ", bg="light yellow")
    l2.place(x=200,y=260)
    l3 = Label(top, text="100 Notes: ", bg="light yellow")
    l3.place(x=200,y=290)

    t1 = Entry(top)
    t1.place(x=300,y=230)
    t2 = Entry(top)
    t2.place(x=300,y=260)
    t3 = Entry(top)
    t3.place(x=300,y=290)

    # Top level mainloop
    top.mainloop()

upload_img = Image.open("widgets/widget5/app_img.jpg")
upload_img = upload_img.resize((300,300))
# Labels
img = ImageTk.PhotoImage(upload_img)
img_label = Label(root, image=img)
img_label.place(x=180,y=20)

label1 = Label(root, text="Hey User! Welcome to Denomination Counter Application.", bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Button 
btn = Button(root, text="Lets get started", command=show_msg, bg='light green')
btn.place(relx=0.5, y=370, anchor=CENTER)
# Mainloop
root.mainloop()