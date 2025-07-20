# 🚗 Snapwheels - Car Management System

**Snapwheels** is a Python-based graphical user interface (GUI) application designed to manage the inventory of a car dealership. The system provides functionalities for both **users** and **administrators**, offering features such as browsing, searching, sorting, adding, deleting, and updating the availability status of cars.

---

## 📌 Features

### 🔹 User Mode:
- View list of available cars.
- Search cars by brand or model.
- Sort cars by price or availability.
- Navigate using the "Back" button.

### 🔹 Admin Mode:
- Add new cars (brand, model, price, year, availability).
- View entire car list.
- Delete cars from inventory.
- Change car status: Available / Sold Out.
- Navigate back to the main menu.

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter** – GUI development
- **Pandas** – CSV data management
- **CSV module** – Reading and writing data
- **Pillow (PIL)** – For adding background images
- **OS module** – File path management

---

## 🧩 Functionalities and Functions

### ✅ Built-in Functions Used:
- `print()` – Debugging and console outputs
- `open()` – File handling (CSV)
- `len()` – Counting data items

### ✅ User-Defined Functions:
- `add_car()` – Add a new car to the CSV and refresh the table.
- `delete_car()` – Remove a selected car from the system.
- `change_status()` – Toggle between "Available" and "Sold Out".
- `search_cars()` – Filter cars based on brand/model.
- `sort_cars()` – Sort car list by price or availability.
- `load_car_data()` – Load and display car data at startup.
- `save_car_data()` – Save changes back to the CSV file.

---

## 🧪 Testing

All functions were tested to ensure they work correctly:
- User/Admin menu buttons
- Add, delete, change status
- Search and sort operations
- GUI navigation
- Error handling (missing fields, invalid file paths, etc.)

---

## 🖼️ GUI Overview

- Main Menu with background image
- Separate interfaces for User and Admin
- Car list displayed using Treeview
- Forms and buttons styled for clarity
- Screenshots can be found in the `/screenshots` folder (add your images here)

---

## 📈 Future Improvements

- Add database support (e.g., SQLite or MySQL) for better scalability and performance.
- Implement login authentication for Admin to enhance security.
- Export reports or inventory as PDF or Excel.
- Improve GUI with responsive layout and dark mode.
- Add confirmation dialogs before deleting cars or changing status.
- Enhance search and filtering with advanced options (e.g., year range, price range).

---

## 🔮 Future Scope

- 🌐 **Web-Based Version**: Transform the desktop app into a web-based system using Flask or Django to make it accessible from anywhere.
- 📱 **Mobile Application**: Create an Android/iOS app version for quick access to inventory on mobile.
- 📊 **Analytics Dashboard**: Integrate data visualization to show car availability trends, sales reports, and pricing statistics.
- 🧠 **AI Integration**: Use machine learning for car price prediction or recommending cars based on user preferences.
- 💾 **Cloud Integration**: Store data on cloud platforms for real-time updates and multi-user access.
- 🧾 **Billing Module**: Add invoice generation and customer billing features.

---

## 📚 References

- [Python Documentation](https://docs.python.org/3/)
- [Tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Pillow Docs](https://pillow.readthedocs.io/)
- [CSV Module Docs](https://docs.python.org/3/library/csv.html)
- [W3Schools Python](https://www.w3schools.com/python/)
- [GeeksforGeeks - Tkinter](https://www.geeksforgeeks.org/python-gui-tkinter/)
