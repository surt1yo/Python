from tkinter import *
import math

def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(value))

def button_click_wrapper(value):
    button_click(value)

def button_clear():
    entry.delete(0, END)

def button_equals():
    try:
        expression = entry.get().replace('÷', '/').replace('×', '*')
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_sqrt():
    try:
        value = float(entry.get())
        if value < 0:
            entry.delete(0, END)
            entry.insert(0, "Error")
        else:
            entry.delete(0, END)
            entry.insert(0, math.sqrt(value))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_square():
    try:
        value = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, value ** 2)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_percent():
    try:
        value = float(entry.get())
        entry.delete(0, END)
        entry.insert(0, value / 100)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Main window
window = Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Display entry
entry = Entry(window, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="ew")

# Buttons frame
buttons_frame = Frame(window)
buttons_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

# Button layout
buttons = [
    ('C', button_clear), ('√', button_sqrt), ('x²', button_square), ('%', button_percent),
    (7, button_click), (8, button_click), (9, button_click), ('÷', button_click),
    (4, button_click), (5, button_click), (6, button_click), ('×', button_click),
    (1, button_click), (2, button_click), (3, button_click), ('-', button_click),
    (0, button_click), ('.', button_click), ('=', button_equals), ('+', button_click)
]

row, col = 0, 0
for (text, command) in buttons:
    if text == '=':
        Button(buttons_frame, text=text, font=("Arial", 16), command=command, bg="lightblue", width=4, height=2).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    elif command == button_click:
        Button(buttons_frame, text=text, font=("Arial", 16), command=lambda v=text: button_click(v), bg="lightgray", width=4, height=2).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    else:
        Button(buttons_frame, text=text, font=("Arial", 16), command=command, bg="lightgray", width=4, height=2).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    buttons_frame.grid_columnconfigure(i, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()