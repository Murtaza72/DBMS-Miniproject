import tkinter
from tkinter import Frame, Label, LabelFrame, Entry, messagebox, ttk, font

from main import BG

BUTTON_BG = "#008001"

window = tkinter.Tk()
window.title("Stock")
window.configure(bg=BG)

# Changing default font size globally
window.defaultFont = font.nametofont("TkDefaultFont")
window.defaultFont.configure(family="Arial", size=15)

main_frame = Frame(window, bg=BG)
main_frame.grid(row=0, column=0)

header_label = Label(main_frame, text="Stock Table",
                     font=("Arial", 25, "bold"), bg=BG)
header_label.grid(row=0, column=0, padx=20, pady=20)


# Header Frame

header_frame = Frame(main_frame, bg=BG)
header_frame.grid(row=1, column=0)

hospital_labelframe = LabelFrame(
    header_frame, text="Stock Information", bg=BG)
hospital_labelframe.grid(row=1, column=0, padx=20, pady=10)

hospital_id_label = Label(
    hospital_labelframe, text="Medicine ID", bg=BG)
hospital_id_label.grid(row=0, column=0, padx=20, pady=10)

hospital_name_label = Label(
    hospital_labelframe, text="Medicine Name", bg=BG)
hospital_name_label.grid(row=1, column=0, padx=20, pady=10)

mfg_date_label = Label(
    hospital_labelframe, text="Mfg Date", bg=BG)
mfg_date_label.grid(row=2, column=0, padx=20, pady=10)

exp_date_label = Label(
    hospital_labelframe, text="Expiry Date", bg=BG)
exp_date_label.grid(row=3, column=0, padx=20, pady=10)

disease_label = Label(
    hospital_labelframe, text="Disease", bg=BG)
disease_label.grid(row=4, column=0, padx=20, pady=10)

stock_label = Label(
    hospital_labelframe, text="Stock", bg=BG)
stock_label.grid(row=5, column=0, padx=20, pady=10)

hospital_id_entry = Entry(hospital_labelframe)
hospital_name_entry = Entry(hospital_labelframe)
mfg_date_entry = Entry(hospital_labelframe)
exp_date_entry = Entry(hospital_labelframe)
disease_entry = Entry(hospital_labelframe)
stock_entry = Entry(hospital_labelframe)

hospital_id_entry.grid(row=0, column=1, padx=10, pady=0)
hospital_name_entry.grid(row=1, column=1, padx=10, pady=0)
mfg_date_entry.grid(row=2, column=1, padx=10, pady=0)
exp_date_entry.grid(row=3, column=1, padx=10, pady=0)
disease_entry.grid(row=4, column=1, padx=10, pady=0)
stock_entry.grid(row=5, column=1, padx=10, pady=0)


def add():
    h_id = hospital_id_entry.get()
    h_name = hospital_name_entry.get()

    print("Added")
    print("ID:", h_id)
    print("Name:", h_name)


def delete_():
    print("Deleted")


def update():
    print("Updated")


def display():
    print("Displayed")


def reset():
    # delete takes first and last index of text to be cleared
    hospital_id_entry.delete(0, "end")
    hospital_name_entry.delete(0, "end")
    mfg_date_entry.delete(0, "end")
    exp_date_entry.delete(0, "end")
    disease_entry.delete(0, "end")
    stock_entry.delete(0, "end")


# Button Frame

button_frame = Frame(main_frame, bg=BG)
button_frame.grid(row=2, column=0, padx=10, pady=10)

add_button = tkinter.Button(button_frame, text=" Add ",
                            command=add, bg=BUTTON_BG)
add_button.grid(row=0, column=0, sticky="news", pady=10)

delete_button = tkinter.Button(button_frame, text="Delete",
                               command=delete_, bg=BUTTON_BG)
delete_button.grid(row=0, column=1, sticky="news", pady=10)

update_button = tkinter.Button(button_frame, text="Update",
                               command=update, bg=BUTTON_BG)
update_button.grid(row=0, column=2, sticky="news", pady=10)

display_button = tkinter.Button(button_frame, text="Display",
                                command=display, bg=BUTTON_BG)
display_button.grid(row=0, column=3, sticky="news", pady=10)

reset_button = tkinter.Button(button_frame, text="Reset",
                              command=reset, bg=BUTTON_BG)
reset_button.grid(row=0, column=4, sticky="news", pady=10)

exit_button = tkinter.Button(button_frame, text=" Exit ",
                             command=exit, bg="#FF0000")
exit_button.grid(row=0, column=5, sticky="news", pady=10)


# Table frame

table_frame = Frame(main_frame, bg=BG)
table_frame.grid(row=3, column=0, padx=20, pady=20)

table_labelframe = LabelFrame(table_frame, text="Table Information", bg=BG)
table_labelframe.grid(row=0, column=0, pady=10)

id_label = Label(table_labelframe, text="ID", bg=BG)
id_label.grid(row=0, column=0, padx=30, pady=20)

name_label = Label(table_labelframe, text="Name", bg=BG)
name_label.grid(row=0, column=1, padx=30, pady=20)

mfg_label = Label(table_labelframe, text="Mfg", bg=BG)
mfg_label.grid(row=0, column=2, padx=30, pady=20)

exp_label = Label(table_labelframe, text="Expiry", bg=BG)
exp_label.grid(row=0, column=3, padx=30, pady=20)

disease_label = Label(table_labelframe, text="Disease", bg=BG)
disease_label.grid(row=0, column=4, padx=30, pady=20)

stock_label = Label(table_labelframe, text="Stock", bg=BG)
stock_label.grid(row=0, column=5, padx=30, pady=20)

window.resizable(False, False)
window.mainloop()
