import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox

# Class
class RestaurantOrderManagement:
    def __init__(self, root):
        self.root=root
        self.root.title("Restaurant Order Management")

        # Dictionary of menu items
        self.menu_items = {
            "FRIES": 5.99,
            "BURGER": 8.99,
            "PIZZA": 12.99,
            "SODA": 1.99,
            "SALAD": 6.99
        }       
        self.exchange_rates = 82.0  
        self.setup_bg(root)
        # Frames
        # Create a frame to hold the widgets
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the frame

        # Heading label
        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        # Dictionaries to store labels and entry references
        self.menu_labels = {}
        self.menu_quantities = {}

        # Create labels and entry widgets for each menu item
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = tk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

            # Button to place the order
        order_button = ttk.Button(frame,text="Place Order",command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2,columnspan=3,padx=10,pady=10)
        
    def setup_bg(self, root):
        canvas = tk.Canvas(root, width=800, height=600)
        canvas.place(x=0, y=0)

        self.bg_image = tk.PhotoImage("restaurant.png")
        print("Image loaded:", self.bg_image.width(), self.bg_image.height())
        canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

    def place_order(self,root):
        

# Block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()

