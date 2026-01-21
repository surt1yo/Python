import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        answer = num1 * num2
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(answer))
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Multiplication Calculator")
root.geometry("400x300")
root.configure(bg='black')

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 300
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Description label
desc_label = tk.Label(root, text="Enter two numbers to calculate their answer:", bg='black', fg='white')
desc_label.grid(row=0, column=0, columnspan=2, pady=10)

# First number label and entry
label1 = tk.Label(root, text="First number:", bg='black', fg='white')
label1.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry1 = tk.Entry(root, bg='gray20', fg='white', insertbackground='white')
entry1.grid(row=1, column=1, padx=10, pady=5)

# Second number label and entry
label2 = tk.Label(root, text="Second number:", bg='black', fg='white')
label2.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry2 = tk.Entry(root, bg='gray20', fg='white', insertbackground='white')
entry2.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate Answer", command=calculate_product, bg='gray30', fg='white')
calc_button.grid(row=3, column=0, columnspan=2, pady=20)

# Result text box
result_label = tk.Label(root, text="Answer:", bg='black', fg='white')
result_label.grid(row=4, column=0, sticky="w", padx=10)
result_text = tk.Text(root, height=4, width=30, bg='gray20', fg='white', insertbackground='white')
result_text.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Run the application
root.mainloop()
