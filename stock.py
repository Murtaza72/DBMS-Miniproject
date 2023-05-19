from tkinter import StringVar

import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.dialogs.dialogs import Messagebox
from ttkbootstrap.widgets import DateEntry

import mysql.connector as mysql

from main import DATABASE_NAME, PASSWORD, THEME

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
    window.title("Stock")

    window.style.configure('.', font=('Arial', 12))

    main_frame = ttk.Frame(window)
    main_frame.grid(row=0, column=0)

    header_label = ttk.Label(main_frame, text="Stock Table",
                             font=("Arial", 25, "bold"))
    header_label.grid(row=0, column=0, padx=20, pady=20)

    # Header Frame

    header_frame = ttk.Frame(main_frame)
    header_frame.grid(row=1, column=0)

    hospital_labelframe = ttk.LabelFrame(
        header_frame, text="Stock Information")
    hospital_labelframe.grid(row=1, column=0, padx=20, pady=10)

    hospital_name_label = ttk.Label(
        hospital_labelframe, text="Medicine Name")
    hospital_name_label.grid(row=1, column=0, padx=20, pady=10)

    mfg_date_label = ttk.Label(
        hospital_labelframe, text="Mfg Date")
    mfg_date_label.grid(row=2, column=0, padx=20, pady=10)

    exp_date_label = ttk.Label(
        hospital_labelframe, text="Expiry Date")
    exp_date_label.grid(row=3, column=0, padx=20, pady=10)

    disease_label = ttk.Label(
        hospital_labelframe, text="Disease")
    disease_label.grid(row=4, column=0, padx=20, pady=10)

    stock_label = ttk.Label(
        hospital_labelframe, text="Stock")
    stock_label.grid(row=5, column=0, padx=20, pady=10)

    stock_label = ttk.Label(
        hospital_labelframe, text="Rate")
    stock_label.grid(row=6, column=0, padx=20, pady=10)

    hospital_name_entry = ttk.Entry(hospital_labelframe)

    mfg_date_entry = DateEntry(
        hospital_labelframe, dateformat="%Y-%m-%d", width=15)
    exp_date_entry = DateEntry(
        hospital_labelframe, dateformat="%Y-%m-%d", width=15)

    disease_drop = StringVar()
    disease_drop.set("Select Disease")

    disease_entry = ttk.Combobox(
        hospital_labelframe, width=18, textvariable=disease_drop, style='info.TCombobox')
    disease_entry["values"] = (
        "Polio", "Covid-19", "Chicken Pox", "Hepatisis B", "Tuberculosis")

    stock_entry = ttk.Entry(hospital_labelframe)
    rate_entry = ttk.Entry(hospital_labelframe)

    hospital_name_entry.grid(row=1, column=1, padx=10, pady=0)
    mfg_date_entry.grid(row=2, column=1, padx=10, pady=0)
    exp_date_entry.grid(row=3, column=1, padx=10, pady=0)

    disease_entry.grid(row=4, column=1, padx=10, pady=0)
    disease_entry.current()

    stock_entry.grid(row=5, column=1, padx=10, pady=0)
    rate_entry.grid(row=6, column=1, padx=10, pady=0)

    def add():
        m_name = hospital_name_entry.get()
        m_mfg = mfg_date_entry.entry.get()
        m_exp = exp_date_entry.entry.get()
        disease = disease_drop.get()
        m_stk = stock_entry.get()
        m_rate = rate_entry.get()
        q1 = "CALL insert_into_stock('{}','{}','{}','{}',{},{});".format(
            str(m_name), str(m_mfg), str(m_exp), str(disease), m_stk, m_rate)
        cursor.execute(q1)
        db.commit()
        print(cursor.rowcount, "records inserted into table!!")
        print("Added")
        display()

    def delete_():
        m_name = hospital_name_entry.get()
        q2 = "CALL delete_from_stocks('{}');".format(m_name)
        cursor.execute(q2)
        db.commit()
        print("Deleted")
        display()

    def update():
        m_name = hospital_name_entry.get()
        m_mfg = mfg_date_entry.get()
        m_exp = exp_date_entry.get()
        disease = disease_drop.get()
        m_stk = stock_entry.get()
        m_rate = rate_entry.get()
        q3 = "update stock set M_mfg='{}',M_exp='{}',Disease='{}',M_stock={},RATE={} where M_name='{}';".format(
            str(m_mfg), str(m_exp), str(disease), str(m_stk), str(m_rate), str(m_name))
        cursor.execute(q3)
        db.commit()
        print("Updated")
        display()

    def display():
        q2 = "CALL update_status();"
        cursor.execute(q2)
        db.commit()
        cursor.execute("SELECT * FROM stock")

        data = cursor.fetchall()

        stock_table = ttk.LabelFrame(main_frame, text="Table Information")
        stock_table.grid(row=3, column=0, padx=20, pady=10)

        headers = [{"text": "Vaccine ID", "stretch": False},
                   {"text": "Vaccine Name", "stretch": True},
                   {"text": "Mfg Date", "stretch": True},
                   {"text": "Expiry Date", "stretch": True},
                   {"text": "Disease", "stretch": True},
                   {"text": "Stock", "stretch": True},
                   {"text": "Rate", "stretch": True},
                   {"text": "Status", "stretch": True}]

        table = Tableview(stock_table,
                          bootstyle="INFO",
                          coldata=headers,
                          rowdata=data,
                          height=5)

        table.autofit_columns()
        table.grid(row=0, column=0, padx=20, pady=20)

    def reset():
        # delete takes first and last index of text to be cleared
        hospital_name_entry.delete(0, "end")
        mfg_date_entry.entry.delete(0, "end")
        exp_date_entry.entry.delete(0, "end")
        disease_drop.set("Select Disease")
        stock_entry.delete(0, "end")
        rate_entry.delete(0, "end")

    # Button Frame

    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=2, column=0, padx=10, pady=10)

    add_button = ttk.Button(button_frame, text=" Add ",
                            command=add)
    add_button.grid(row=0, column=0, sticky="news", padx=1, pady=10)

    delete_button = ttk.Button(button_frame, text="Delete",
                               command=delete_)
    delete_button.grid(row=0, column=1, sticky="news", padx=1, pady=10)

    update_button = ttk.Button(button_frame, text="Update",
                               command=update)
    update_button.grid(row=0, column=2, sticky="news", padx=1, pady=10)

    display_button = ttk.Button(button_frame, text="Display",
                                command=display)
    display_button.grid(row=0, column=3, sticky="news", padx=1, pady=10)

    reset_button = ttk.Button(button_frame, text="Reset",
                              command=reset)
    reset_button.grid(row=0, column=4, sticky="news", padx=1, pady=10)

    exit_button = ttk.Button(button_frame, text=" Exit ",
                             command=exit, bootstyle="DANGER")
    exit_button.grid(row=0, column=5, sticky="news", padx=1, pady=10)

    window.resizable(False, False)
    window.mainloop()
