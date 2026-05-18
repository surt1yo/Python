# Write a Python program to create an application 
# to play a rock paper scissor game between a user 
# and the computer, using the Python Tkinter library.
import tkinter as tk
import random
from tkinter import ttk, messagebox
# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Function to handle the game logic
def play_rps(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
        
    messagebox.showinfo("Game Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

# Create buttons for user choices
rock_button = ttk.Button(root, text="Rock", command=lambda: play_rps("Rock"))
rock_button.pack(pady=10)
paper_button = ttk.Button(root, text="Paper", command=lambda: play_rps("Paper"))
paper_button.pack(pady=10)
scissors_button = ttk.Button(root, text="Scissors", command=lambda: play_rps("Scissors"))
scissors_button.pack(pady=10)

root.mainloop()