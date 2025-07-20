import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import BOTH, END
import pandas as pd
import os
from PIL import Image, ImageTk


class Snapwheels:
    def __init__(self, root):
        self.root = root
        self.root.title("Snapwheels")
        self.root.geometry("1500x1000")
        self.cars = []
        self.load_cars()

        self.frames = {}

        self.create_role_selection()

    def create_role_selection(self):
        """Create the role selection menu with background image."""
        self.clear_window()

        self.bg_image = ImageTk.PhotoImage(
            Image.open("/Users/atharvmundhe/PycharmProjects/PythonProject/aston.jpg").resize((1500, 1000)))
        # Canvas for background
        canvas = tk.Canvas(self.root, width=1500, height=1000)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Create a frame on top of the canvas
        role_frame = tk.Frame(canvas, bg="black", bd=2)
        role_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(role_frame, text="   Welcome to Snapwheels   ", font=("Didot", 25), bg="black").pack(pady=20)
        ttk.Button(role_frame, text=" User ", width=20, command=self.show_user_page).pack(pady=10)
        ttk.Button(role_frame, text=" Admin ", width=20, command=self.show_admin_menu).pack(pady=10)
        ttk.Button(role_frame, text=" Exit ", width=10, command=self.exit_application).pack(pady=10)

        self.frames["role_selection"] = canvas

    def exit_application(self):
        self.root.quit()

    def show_user_page(self):
        """Display the user page."""
        self.clear_window()

        user_frame = ttk.Frame(self.root)
        user_frame.pack(fill=BOTH, expand=True)

        ttk.Label(user_frame, text="USER", font=("Didot", 20)).pack(pady=5)

        search_frame = ttk.Frame(user_frame)
        search_frame.pack(fill="x", padx=10, pady=20)
        ttk.Label(search_frame, text="Search:").pack(side="left")
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Go", command=self.search_cars).pack(side="left", padx=1)

        # Sort by options
        ttk.Label(search_frame, text="    Sort By:").pack(side="left", padx=5)
        self.sort_var = tk.StringVar()
        sort_menu = ttk.Combobox(search_frame, textvariable=self.sort_var,
                                 values=["Price: Low to High", "Price: High to Low", "Available", "Sold Out"])
        sort_menu.set("Price: Low to High")
        sort_menu.pack(side="left", padx=1)
        sort_menu.bind("<<ComboboxSelected>>", self.sort_cars)

        self.user_tree = ttk.Treeview(user_frame, columns=("Brand", "Model", "Price(£)", "Year", "Status"),
                                      show="headings")
        for col in ("Brand", "Model", "Price(£)", "Year", "Status"):
            self.user_tree.heading(col, text=col, command=lambda c=col: self.sort_column(self.user_tree, c))
        self.user_tree.pack(fill=BOTH, expand=True)

        self.display_cars(self.user_tree)

        back_button = ttk.Button(user_frame, text="Back", command=self.create_role_selection)
        back_button.pack(side="bottom", pady=10)

        self.frames["user"] = user_frame

    def sort_cars(self, event=None):
        """Sort the cars based on the selected sort option."""
        sort_option = self.sort_var.get()
        if sort_option == "Price: Low to High":
            self.cars.sort(key=lambda car: car["price(£)"])
        elif sort_option == "Price: High to Low":
            self.cars.sort(key=lambda car: car["price(£)"], reverse=True)
        elif sort_option == "Available":
            self.cars.sort(key=lambda car: car["availability"] == "Available", reverse=True)
        elif sort_option == "Sold Out":
            self.cars.sort(key=lambda car: car["availability"] == "Sold Out", reverse=True)

        self.display_cars(self.user_tree)

    def show_admin_menu(self):
        """Display admin main menu with options."""
        self.clear_window()
        self.bg_image = ImageTk.PhotoImage(
            Image.open("/Users/atharvmundhe/PycharmProjects/PythonProject/pic1.jpg").resize((1500,1000)))


        # Canvas for background
        canvas = tk.Canvas(self.root, width=1500, height=1000)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Create a frame for admin menu
        admin_frame = tk.Frame(canvas, bg="black", bd=2)
        admin_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(admin_frame, text="      Admin Menu      ", font=("Didot", 25), bg="black").pack(pady=20)

        ttk.Button(admin_frame, text=" Add Car ", width=20, command=self.show_add_car_form).pack(pady=10)
        ttk.Button(admin_frame, text=" My Cars ", width=20, command=self.my_cars).pack(pady=10)
        ttk.Button(admin_frame, text=" Back ", width=10, command=self.create_role_selection).pack(pady=10)

        self.frames["admin_menu"] = canvas

    def show_add_car_form(self):
        """Display the form for adding a new car."""
        self.clear_window()
        self.bg_image = ImageTk.PhotoImage(
            Image.open("/Users/atharvmundhe/PycharmProjects/PythonProject/pic1.jpg").resize((1500, 1000)))
        form_frame = ttk.Frame(self.root)
        form_frame.pack(fill=BOTH, expand=True)
        # Canvas for background
        canvas = tk.Canvas(self.root, width=1500, height=1000)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Create a frame on top of the canvas
        form_frame = tk.Frame(canvas, bg="black", bd=2)
        form_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(form_frame, text="Add New Car", font=("Arial", 20)).pack(pady=20)

        fields = ["Brand", "Model", "Price(£)", "Year"]
        self.entries = {}
        for field in fields:
            row = ttk.Frame(form_frame)
            row.pack(fill="x", pady=5, padx=10)
            ttk.Label(row, text=field + ":", width=15).pack(side="left")
            entry = ttk.Entry(row)
            entry.pack(side="left", fill="x", expand=True)
            self.entries[field.lower()] = entry

        # Dropdown for availability
        row = ttk.Frame(form_frame)
        row.pack(fill="x", pady=5, padx=10)
        ttk.Label(row, text="Availability:", width=15).pack(side="left")
        self.availability_var = tk.StringVar()
        availability_dropdown = ttk.Combobox(row, textvariable=self.availability_var, state="readonly")
        availability_dropdown['values'] = ("Available", "Sold Out")
        availability_dropdown.current(0)
        availability_dropdown.pack(side="left", fill="x", expand=True)
        self.entries["availability"] = availability_dropdown  # Add to entries dictionary

        ttk.Button(form_frame, text="Add Car", command=self.add_car).pack(pady=15)
        ttk.Button(form_frame, text="Back", command=self.show_admin_menu).pack(pady=10)

        self.frames["add_car"] = canvas

    def add_car(self):
        """Add a new car to the list."""
        try:
            brand = self.entries["brand"].get().strip()
            model = self.entries["model"].get().strip()
            price = float(self.entries["price(£)"].get())
            year = int(self.entries["year"].get())
            availability = self.entries["availability"].get().strip()

            if not all([brand, model, price, year, availability]):
                raise ValueError("All fields must be filled.")

            if any(car["brand"] == brand and car["model"] == model for car in self.cars):
                raise ValueError("This car already exists.")

            new_car = {"brand": brand, "model": model, "price(£)": price, "year": year, "availability": availability}
            self.cars.append(new_car)
            self.save_cars()
            if "admin" in self.frames:
                self.display_cars(self.admin_tree)
            if "user" in self.frames:
                self.display_cars(self.user_tree)

            # Clear input fields
            for entry in self.entries.values():
                entry.delete(0, END)

            # Show success message
            messagebox.showinfo("Success", "Car added successfully!")

        except ValueError as ve:
            messagebox.showwarning("Input Error", str(ve))

    def delete_car(self):
        """Delete the selected car."""
        selected_item = self.admin_tree.selection()
        if selected_item:
            values = self.admin_tree.item(selected_item[0], 'values')
            self.cars = [car for car in self.cars if not (car["brand"] == values[0] and car["model"] == values[1])]
            self.save_cars()
            self.display_cars(self.admin_tree)
            self.display_cars(self.user_tree)
        else:
            messagebox.showinfo("No selection", "Please select a car to delete.")

    def my_cars(self):
        """Display the admin car list."""
        self.clear_window()

        cars_frame = ttk.Frame(self.root)
        cars_frame.pack(fill=BOTH, expand=True)

        self.admin_tree = ttk.Treeview(cars_frame, columns=("Brand", "Model", "Price(£)", "Year", "Status"),
                                       show="headings")
        for col in ("Brand", "Model", "Price(£)", "Year", "Status"):
            self.admin_tree.heading(col, text=col, command=lambda c=col: self.sort_column(self.admin_tree, c))
        self.admin_tree.pack(fill=BOTH, expand=True)

        button_frame = ttk.Frame(cars_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Delete car", command=self.delete_car).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Change Status", command=self.change_status).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back", command=self.show_admin_menu).pack(side="left", padx=5)

        self.display_cars(self.admin_tree)

        self.frames["admin"] = cars_frame

    def clear_window(self):
        """Clear the current frame."""
        for frame in self.frames.values():
            frame.destroy()
        self.frames.clear()

    def display_cars(self, tree):
        """Display the cars in the treeview."""
        tree.delete(*tree.get_children())
        for car in self.cars:
            tree.insert("", END, values=(car["brand"], car["model"], car["price(£)"], car["year"], car["availability"]))

    def change_status(self):
        """Change the availability status of the selected car."""
        selected_item = self.admin_tree.selection()
        if selected_item:
            values = self.admin_tree.item(selected_item[0], 'values')
            for car in self.cars:
                if car["brand"] == values[0] and car["model"] == values[1]:
                    car["availability"] = "Sold Out" if car["availability"] == "Available" else "Available"
                    break
            self.save_cars()
            if "admin" in self.frames:
                self.display_cars(self.admin_tree)
            if "user" in self.frames:
                self.display_cars(self.user_tree)

        else:
            messagebox.showinfo("No selection", "Please select a car to change status.")

    def search_cars(self):
        """Search for cars based on the search input."""
        query = self.search_var.get().lower()
        filtered = [car for car in self.cars if query in car["brand"].lower() or query in car["model"].lower()]
        self.user_tree.delete(*self.user_tree.get_children())
        for car in filtered:
            self.user_tree.insert("", END, values=(
            car["brand"], car["model"], car["price(£)"], car["year"], car["availability"]))

    def sort_column(self, tree, col):
        """Sort the columns."""
        data = [(tree.set(k, col), k) for k in tree.get_children("")]
        try:
            data.sort(key=lambda t: float(t[0]) if col in ["Price(£)", "Year"] else t[0].lower())
        except ValueError:
            data.sort(key=lambda t: t[0].lower())

        for index, (val, k) in enumerate(data):
            tree.move(k, '', index)

    def save_cars(self):
        """Save the car data to a CSV file using pandas."""
        df = pd.DataFrame(self.cars)
        df.to_csv("cars.csv", index=False)

    def load_cars(self):
        """Load the car data from a CSV file using pandas."""
        self.cars = []
        if os.path.exists("cars.csv"):
            try:
                df = pd.read_csv("cars.csv")
                for _, row in df.iterrows():
                    car = {
                        "brand": row["brand"],
                        "model": row["model"],
                        "price(£)": row["price(£)"],
                        "year": row["year"],
                        "availability": row["availability"]
                    }
                    self.cars.append(car)
            except Exception as e:
                messagebox.showerror("Load Error", f"Failed to load car data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Snapwheels(root)
    root.mainloop()


