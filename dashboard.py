import ttkbootstrap as ttk
import mysql.connector as mysql

from main import DATABASE_NAME, PASSWORD, THEME

import mysql.connector as mysql

global d


def start(root):

    db = mysql.connect(host="localhost",
                       user="root",
                       password=PASSWORD)

    d = DATABASE_NAME
    cursor = db.cursor()
    que1 = 'use {}'.format(d)
    cursor.execute(que1)

    if (db.is_connected()):
        print("Connected to MySQL Successfully")
    else:
        print("Error Connecting to MySQL")

    window = ttk.Toplevel(root)
    window.title("Admin Dashboard")

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0)

    header_label = ttk.Label(
        frame, text="Select from the following options", font=("Arial", 15))
    header_label.grid(row=0, column=0, padx=20, pady=10)

    def sales():
        import sales
        sales.start(window)

    def hospital():
        import hospital
        hospital.start(window)

    def stock():
        import stock
        stock.start(window)

    # MonthlySales
    monthly_sales_button = ttk.Button(frame, text="Sales",
                                      command=sales)
    monthly_sales_button.grid(row=1, column=0, sticky="news", padx=20, pady=5)

    # Add and Delete Hospital

    hospital_button = ttk.Button(frame, text="Hospital",
                                 command=hospital)
    hospital_button.grid(row=2, column=0, sticky="news", padx=20, pady=5)

    # Stock Add and Delete
    # Get Stock

    stock_button = ttk.Button(
        frame, text="Stock", command=stock)
    stock_button.grid(row=3, column=0, sticky="news", padx=20, pady=5)

    window.resizable(False, False)
    window.mainloop()
