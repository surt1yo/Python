# Learn to handle keyboard and mouse events in Tkinter! 
# Students will create an interactive application that 
# responds to key presses and button clicks, understanding 
# event-driven programming and event binding concepts.
from tkinter import *

def on_key_press(event):
    print(f"Key pressed: {event.char}")
def button_click(event):
    print("Button was clicked!")    
# Creating the main window
window = Tk()
window.geometry("400x300")
btn = Button(window, text = "Click Me")
btn.pack(pady = 20)

#widget.bind(event_sequence, handler_function, add=None)
window.bind("<Key>", on_key_press,)
btn.bind("<Button-1>", button_click)
window.mainloop()