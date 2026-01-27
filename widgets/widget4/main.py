# Build a fully functional text editor application with Tkinter! 
# Students will learn to create file dialogs, read and write files, 
# use text widgets for editing, and organize layouts 
# with frames and grids. This project demonstrates real-world 
# application development with file handling capabilities.
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
# Create the main window
window = Tk()
window.title("Mezaan's Text Editor")
window.geometry("500x400")

# Rows and Columns Configuration
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# File Handling Functions
def open_file():
    # Making Sure the file is opened in a txt format
    filepath = askopenfilename(
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    text_editor.delete("1.0", END)
    print(filepath)
    with open(filepath, "r") as input_file:
        # Reading the file content
        text = input_file.read()
        print(text)
        text_editor.insert(END, text)
        input_file.close()
    window.title(f"Mezaan's Text Editor - {filepath}")
def save_file():
    filepath = asksaveasfilename(
    defaultextension="txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_editor.get("1.0", END)
        output_file.write(text)
        output_file.close()
    window.title(f"Mezaan's Text Editor - {filepath}")

# Text Editor
text_editor = Text(window)
text_editor.grid(row=0, column=1, sticky="nsew")

# Add widgets in the application
frame1 = Frame(window, relief=RAISED, bd=2)
frame1.grid(row=0, column=0, sticky="ns")

btn_open = Button(frame1, text="Open", command=open_file)
btn_open.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

btn_save = Button(frame1, text="Save As", command=save_file)
btn_save.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

#Main Loop
window.mainloop()