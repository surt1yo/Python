# Create your first GUI window using Tkinter! 
# Students will learn the basics of creating a graphical window, 
# setting its title, and defining its size. This is the foundation for
# building interactive desktop applications.
from tkinter import *
# Create the main window
window = Tk()
window.title("My First GUI Window")
window.geometry("400x300")
window.mainloop()