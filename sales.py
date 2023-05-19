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
    window.title("Sales")

    window.style.configure('.', font=('Arial', 12))

    main_frame = ttk.Frame(window)
    main_frame.grid(row=0, column=0)

    header_label = ttk.Label(main_frame, text="Sales Table",
                             font=("Arial", 25, "bold"))
    header_label.grid(row=0, column=0, padx=20, pady=20)

    header_frame = ttk.Frame(main_frame)
    header_frame.grid(row=1, column=0)

    stock_labelframe = ttk.LabelFrame(
        header_frame, text="Sales Information")
    stock_labelframe.grid(row=1, column=0, padx=20, pady=10)

    hospital_id_label = ttk.Label(
        stock_labelframe, text="Hospital Name")
    hospital_id_label.grid(row=1, column=0, padx=20, pady=10)

    medicine_id_label = ttk.Label(
        stock_labelframe, text="Vaccine Name")
    medicine_id_label.grid(row=2, column=0, padx=20, pady=10)

    qty_label = ttk.Label(
        stock_labelframe, text="Quantity")
    qty_label.grid(row=3, column=0, padx=20, pady=10)

    hospital_id_entry = ttk.Entry(stock_labelframe)
    medicine_id_entry = ttk.Entry(stock_labelframe)
    qty_entry = ttk.Entry(stock_labelframe)

    hospital_id_entry.grid(row=1, column=1, padx=10, pady=0)
    medicine_id_entry.grid(row=2, column=1, padx=10, pady=0)
    qty_entry.grid(row=3, column=1, padx=10, pady=0)

    def add():
        h_id = hospital_id_entry.get()
        m_id = medicine_id_entry.get()
        qty = qty_entry.get()

        q = "select count(*) from partial_order;"
        cursor.execute(q)
        data1 = cursor.fetchall()[0]

        q1 = "CALL insert_into_sales('{}','{}',{});".format(m_id, h_id, qty)
        cursor.execute(q1)

        # Consume unread results
        cursor.fetchall()

        cursor.execute(
            "select Status from stock where M_name='{}';".format(m_id))
        val = cursor.fetchall()
        if val[0][0] == "Expired":
            Messagebox.show_warning(
                title="Warning", message="Vaccine is expired!!")

        q2 = "select count(*) from partial_order;"
        cursor.execute(q2)
        data2 = cursor.fetchall()[0]
        db.commit()

        if data2 > data1:
            Messagebox.show_info(message="Some partial orders there!!")
            cursor.execute("CALL update_partial()")
            db.commit()
        display()

    def display():
        cursor.execute("SELECT * FROM sales;")
        data = cursor.fetchall()

        sales_table = ttk.LabelFrame(main_frame, text="Table Information")
        sales_table.grid(row=3, column=0, padx=20, pady=10)

        headers = [{"text": "Batch ID", "stretch": False},
                   {"text": "Hospital ID", "stretch": False},
                   {"text": "Vaccine ID", "stretch": False},
                   {"text": "Quantity", "stretch": True},
                   {"text": "Order Date", "stretch": True},
                   {"text": "Total Price", "stretch": True}]

        table = Tableview(sales_table,
                          bootstyle="INFO",
                          coldata=headers,
                          rowdata=data,
                          height=6)

        table.autofit_columns()
        table.grid(row=0, column=0, padx=20, pady=20)

    def reset():
        hospital_id_entry.delete(0, "end")
        medicine_id_entry.delete(0, "end")
        qty_entry.delete(0, "end")

    def show_sale():
        root = ttk.Toplevel(title="Sales Table")
        root.resizable(False, False)

        month_sale_frame = ttk.LabelFrame(root, text="Table Information")
        month_sale_frame.grid(row=0, column=0, padx=20, pady=10)

        q1 = "CALL getmonthlysales();"
        cursor.execute(q1)
        data = cursor.fetchall()

        header = ["Vaccine Name", "Total Price"]
        headers = [
            {"text": "Vaccine Name", "stretch": True},
            {"text": "Total Price", "stretch": True}]

        table = Tableview(month_sale_frame,
                          bootstyle="INFO",
                          coldata=headers,
                          rowdata=data,
                          height=5)

        table.autofit_columns()
        table.grid(row=0, column=0, padx=20, pady=20)

    def partial_order():
        root = ttk.Toplevel(title="Partial Orders Table")
        root.resizable(False, False)

        partial_order_frame = ttk.LabelFrame(root, text="Table Information")
        partial_order_frame.grid(row=0, column=0, padx=20, pady=10)

        q1 = "SELECT * FROM partial_order;"
        cursor.execute(q1)
        data = cursor.fetchall()

        headers = [
            {"text": "Hospital ID", "stretch": False},
            {"text": "Vaccine ID", "stretch": False},
            {"text": "Quantity Left", "stretch": True}]

        table = Tableview(partial_order_frame,
                          bootstyle="INFO",
                          coldata=headers,
                          rowdata=data,
                          height=5)

        table.autofit_columns()
        table.grid(row=0, column=0, padx=20, pady=20)

    def expire():
        root = ttk.Toplevel(title="Expired Table")
        root.resizable(False, False)

        expired_table = ttk.LabelFrame(root, text="Table Information")
        expired_table.grid(row=0, column=0, padx=20, pady=10)

        cursor.execute("SELECT * FROM expired")
        data = cursor.fetchall()

        headers = [
            {"text": "Vaccine ID", "stretch": False},
            {"text": "Vaccine Name", "stretch": True},
            {"text": "Expiry Date", "stretch": True}]

        table = Tableview(expired_table,
                          bootstyle="INFO",
                          coldata=headers,
                          rowdata=data,
                          height=10)

        table.autofit_columns()
        table.grid(row=0, column=0, padx=20, pady=20)

    # Button Frame

    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=2, column=0, padx=10, pady=10)

    add_button = ttk.Button(button_frame, text=" Add ",
                            command=add)
    add_button.grid(row=0, column=0, sticky="news", padx=1, pady=5)

    display_button = ttk.Button(button_frame, text="Display",
                                command=display)
    display_button.grid(row=0, column=1, sticky="news", padx=1, pady=5)

    reset_button = ttk.Button(button_frame, text="Reset",
                              command=reset)
    reset_button.grid(row=0, column=2, sticky="news", padx=1, pady=5)

    sale_button = ttk.Button(button_frame, text="Monthly Sales",
                             command=show_sale)
    sale_button.grid(row=0, column=3, sticky="news", padx=1, pady=5)

    expired_button = ttk.Button(
        button_frame, text="Expired Stock", command=expire)
    expired_button.grid(row=0, column=5, sticky="news", padx=1, pady=5)

    exit_button = ttk.Button(button_frame, text=" Exit ",
                             command=exit, bootstyle="DANGER")
    exit_button.grid(row=0, column=6, sticky="news", padx=1, pady=5)

    window.resizable(False, False)
    window.mainloop()
