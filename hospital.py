import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.dialogs.dialogs import Messagebox
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
    window.title("Hospital")

    window.style.configure('.', font=('Arial', 12))

    main_frame = ttk.Frame(window)
    main_frame.grid(row=0, column=0)

    header_label = ttk.Label(main_frame, text="Hospital Table",
                             font=("Arial", 25, "bold"))
    header_label.grid(row=0, column=0, padx=20, pady=20)

    # Header Frame

    header_frame = ttk.Frame(main_frame)
    header_frame.grid(row=1, column=0)

    hospital_labelframe = ttk.LabelFrame(
        header_frame, text="Hospital Information")
    hospital_labelframe.grid(row=1, column=0, padx=20, pady=10)

    hospital_name_label = ttk.Label(
        hospital_labelframe, text="Hospital Name")
    hospital_name_label.grid(row=0, column=0, padx=10, pady=10)

    hospital_con_label = ttk.Label(
        hospital_labelframe, text="Hospital Contact")
    hospital_con_label.grid(row=1, column=0, padx=10, pady=10)

    hospital_name_entry = ttk.Entry(hospital_labelframe)
    hospital_con_entry = ttk.Entry(hospital_labelframe)

    hospital_name_entry.grid(row=0, column=1, padx=10, pady=10)
    hospital_con_entry.grid(row=1, column=1, padx=10, pady=10)

    def add():
        h_con = hospital_con_entry.get()
        h_name = hospital_name_entry.get()

        if (len(h_con) == 10) and h_con.isdigit() and h_name:
            print("Added")
            # print("ID:", h_id)
            # print("Name:", h_name)
            q1 = "CALL insert_into_hospital('{}','{}');".format(h_name, h_con)
            cursor.execute(q1)
            db.commit()
            print(cursor.rowcount, "record inserted.")

        else:
            Messagebox.show_warning(
                title="Warning", message="Name and Phone number are required(10 digits).")

        reset()
        display()

    def delete_():
        h_name = hospital_name_entry.get()
        q1 = "CALL delete_from_hospital('{}');".format(h_name)
        cursor.execute(q1)
        db.commit()
        print("Deleted")

        reset()

    def update():
        h_con = hospital_con_entry.get()
        h_name = hospital_name_entry.get()
        q1 = "update Hospital set H_contact='{}' where H_name='{}';".format(
            h_con, h_name)
        cursor.execute(q1)
        print("Updated")

        display()

    def display():

        hospital_table = ttk.LabelFrame(
            main_frame, text="Table Information")
        hospital_table.grid(row=3, column=0, padx=20, pady=10)

        cursor.execute("SELECT * FROM hospital")
        data = cursor.fetchall()

        headers = [{"text": "ID", "stretch": False},
                   {"text": "Hospital Name", "stretch": True},
                   {"text": "Contact", "stretch": False}]

        table = Tableview(hospital_table,
                          bootstyle="INFO",
                          coldata=headers,
                          rowdata=data,
                          height=5)

        table.autofit_columns()
        table.grid(row=0, column=0, padx=20, pady=20)

    def reset():
        hospital_con_entry.delete(0, "end")
        hospital_name_entry.delete(0, "end")

    def show_hosp_sale():
        root = ttk.Toplevel(title="Sales Table")
        root.resizable(False, False)

        expired_table = ttk.LabelFrame(root, text="Table Information")
        expired_table.grid(row=0, column=0, padx=20, pady=10)

        q1 = "CALL gethospsales2();"
        cursor.execute(q1)
        data = cursor.fetchall()

        headers = [
            {"text": "Batch ID", "stretch": False},
            {"text": "Hospital ID", "stretch": False},
            {"text": "Hospital Name", "stretch": True},
            {"text": "Revenue", "stretch": True}]

        table = Tableview(expired_table,
                          bootstyle="INFO",
                          coldata=headers,
                          rowdata=data,
                          height=5)

        table.autofit_columns()
        table.grid(row=0, column=0, padx=20, pady=20)

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

    sale_button = ttk.Button(button_frame, text=" Sales ",
                             command=show_hosp_sale)
    sale_button.grid(row=0, column=5, sticky="news", padx=1, pady=10)

    exit_button = ttk.Button(button_frame, text=" Exit ",
                             command=exit, bootstyle="DANGER")
    exit_button.grid(row=0, column=6, sticky="news", padx=1, pady=10)

    window.resizable(False, False)
    window.mainloop()
