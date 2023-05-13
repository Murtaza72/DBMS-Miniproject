import tkinter
from tkinter import Frame, Label, LabelFrame, Entry, font

from main import BG, BUTTON_BG

window = tkinter.Tk()
window.title("Sales")
window.configure(bg=BG)

window.defaultFont = font.nametofont("TkDefaultFont")
window.defaultFont.configure(family="Arial", size=15)

main_frame = Frame(window, bg=BG)
main_frame.grid(row=0, column=0)

header_label = Label(main_frame, text="Sales Table",
                     font=("Arial", 25, "bold"), bg=BG)
header_label.grid(row=0, column=0, padx=20, pady=20)


header_frame = Frame(main_frame, bg=BG)
header_frame.grid(row=1, column=0)

stock_labelframe = LabelFrame(
    header_frame, text="Sales Information", bg=BG)
stock_labelframe.grid(row=1, column=0, padx=20, pady=10)

batch_id_label = Label(
    stock_labelframe, text="Batch ID", bg=BG)
batch_id_label.grid(row=0, column=0, padx=20, pady=10)

hospital_id_label = Label(
    stock_labelframe, text="Hospital ID", bg=BG)
hospital_id_label.grid(row=1, column=0, padx=20, pady=10)

medicine_id_label = Label(
    stock_labelframe, text="Medicine ID", bg=BG)
medicine_id_label.grid(row=2, column=0, padx=20, pady=10)

qty_label = Label(
    stock_labelframe, text="Quantity", bg=BG)
qty_label.grid(row=3, column=0, padx=20, pady=10)


batch_id_entry = Entry(stock_labelframe)
hospital_id_entry = Entry(stock_labelframe)
medicine_id_entry = Entry(stock_labelframe)
qty_entry = Entry(stock_labelframe)

batch_id_entry.grid(row=0, column=1, padx=10, pady=0)
hospital_id_entry.grid(row=1, column=1, padx=10, pady=0)
medicine_id_entry.grid(row=2, column=1, padx=10, pady=0)
qty_entry.grid(row=3, column=1, padx=10, pady=0)


def add():
    b_id = batch_id_entry.get()
    h_id = hospital_id_entry.get()
    m_id = medicine_id_entry.get()
    qty = qty_entry.get()

    print("Added")
    print("BID:", b_id)
    print("HID:", h_id)
    print("MID:", m_id)
    print("QTY:", qty)


def delete_():
    print("Deleted")


def update():
    print("Updated")


def display():
    print("Displayed")


def reset():
    # delete takes first and last index of text to be cleared
    batch_id_entry.delete(0, "end")
    hospital_id_entry.delete(0, "end")
    medicine_id_entry.delete(0, "end")
    qty_entry.delete(0, "end")


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

bid_label = Label(table_labelframe, text="Batch ID", bg=BG)
bid_label.grid(row=0, column=0, padx=30, pady=20)

hid_label = Label(table_labelframe, text="Hospital ID", bg=BG)
hid_label.grid(row=0, column=1, padx=30, pady=20)

mid_label = Label(table_labelframe, text="Medicine ID", bg=BG)
mid_label.grid(row=0, column=2, padx=30, pady=20)

qty_label = Label(table_labelframe, text="Quantity", bg=BG)
qty_label.grid(row=0, column=3, padx=30, pady=20)

window.resizable(False, False)
window.mainloop()
