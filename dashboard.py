import tkinter
from tkinter import Frame, Label, LabelFrame, Entry, Toplevel, messagebox, ttk

from main import BG

window = tkinter.Tk()
window.title("Admin Dashboard")

frame = Frame(window, bg=BG)
frame.grid(row=0, column=0)

header_label = Label(
    frame, text="Select from the following options", font=("Arial", 15), bg=BG)
header_label.grid(row=0, column=0, padx=20, pady=10)


def sales():
    window.destroy()
    import sales


def hospital():
    window.destroy()
    import hospital


def stock():
    window.destroy()
    import stock


# MonthlySales
monthly_sales_button = tkinter.Button(frame, text="Display Monthly Sales",
                                      command=sales, bg=BG)
monthly_sales_button.grid(row=1, column=0, sticky="news", padx=20, pady=5)


# Add and Delete Hospital

hospital_button = tkinter.Button(frame, text="Add/Delete Hospitals",
                                 command=hospital, bg=BG)
hospital_button.grid(row=2, column=0, sticky="news", padx=20, pady=5)


# Stock Add and Delete
# Get Stock

stock_button = tkinter.Button(
    frame, text="Add/Delete Stock", command=stock, bg=BG)
stock_button.grid(row=3, column=0, sticky="news", padx=20, pady=5)


window.resizable(False, False)
window.mainloop()
