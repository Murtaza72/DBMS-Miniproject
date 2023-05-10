import tkinter
from tkinter import Frame, Label, LabelFrame, Entry, messagebox, ttk
from PIL import ImageTk, Image
import re

# Colors
BG = "#F0FFFF"

window = tkinter.Tk()
window.title("Signup")

frame = Frame(window, bg=BG)
frame.pack()

signup_label = Label(frame, text="Sign Up", font=(
    "Arial", 20, "bold"), bg=BG)
signup_label.grid(row=0, column=0, pady=15)

logo_img = ImageTk.PhotoImage(Image.open("logo.jpg").resize((100, 100)))
logo_label = Label(frame, image=logo_img)
logo_label.grid(row=1, column=0, pady=10)

signup_labelframe = LabelFrame(frame, text="Member Information", bg=BG)
signup_labelframe.grid(row=2, column=0, padx=20, pady=10)

name_label = Label(signup_labelframe, text="Name", bg=BG)
name_label.grid(row=0, column=0, padx=5, pady=5)

age_label = Label(signup_labelframe, text="Age", bg=BG)
age_label.grid(row=0, column=1, padx=5, pady=5)

email_label = Label(signup_labelframe, text="Email", bg=BG)
email_label.grid(row=0, column=2, padx=5, pady=5)

phone_label = Label(signup_labelframe, text="Phone Number", bg=BG)
phone_label.grid(row=2, column=0, padx=5, pady=5)

gender_label = tkinter.Label(signup_labelframe, text="Gender", bg=BG)
gender_combobox = ttk.Combobox(signup_labelframe, values=[
    "", "Male", "Female", "Others"])
gender_label.grid(row=2, column=1)


password_label = Label(signup_labelframe, text="Password", bg=BG)
password_label.grid(row=2, column=2, padx=5, pady=5)

username_entry = Entry(signup_labelframe)
age_entry = tkinter.Entry(signup_labelframe)
email_entry = Entry(signup_labelframe)
phone_entry = Entry(signup_labelframe)
password_entry = Entry(signup_labelframe)

username_entry.grid(row=1, column=0, padx=10, pady=10)
age_entry.grid(row=1, column=1, padx=10, pady=10)
email_entry.grid(row=1, column=2, padx=10, pady=10)
phone_entry.grid(row=3, column=0, padx=10, pady=10)
gender_combobox.grid(row=3, column=1, padx=10, pady=10)
password_entry.grid(row=3, column=2, padx=10, pady=10)


lowercase = "[a-z]"
uppercase = "[A-Z]"
numbers = "[0-9]"


def signup():
    username = username_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_combobox.get()
    password = password_entry.get()

    if username and age and email and phone and gender and password:

        if age.isnumeric() and int(age) >= 18:

            if phone.isnumeric() and len(phone) == 10:

                if (re.search(lowercase, password) and re.search(uppercase, password) and re.search(numbers, password) and len(password) >= 8):
                    print("Username:", username)
                    print("Age:", age)
                    print("Email:", email)
                    print("Phone Number:", phone)
                    print("Gender:", gender)

                else:
                    tkinter.messagebox.showwarning(
                        title="Error", message="Password must contain at least 1 lowercase, 1 uppercase character, 1 number and must be 8 character long")

            else:
                tkinter.messagebox.showwarning(
                    title="Error", message="Phone number should have 10 digits")

        else:
            tkinter.messagebox.showwarning(
                title="Error", message="Age must be above 18")

    else:
        tkinter.messagebox.showwarning(
            title="Error", message="All the field are required")


signup_button = tkinter.Button(frame, text="Submit",
                               command=signup, font=("Arial", 12), bg=BG)
signup_button.grid(row=3, column=0, pady=10)

window.resizable(False, False)
window.mainloop()
