import tkinter
from tkinter import Frame, Label, LabelFrame, Entry, messagebox
from PIL import ImageTk, Image

# Colors
BG = "#F0FFFF"
BUTTON_BG = "#008001"


def main():
    window = tkinter.Tk()

    window.title("Login")
    window.configure(bg=BG)

    frame = Frame(window, bg=BG)
    frame.grid(row=0, column=0)

    login_label = Label(frame, text="Login", font=(
        "Arial", 20, "bold"), bg=BG)
    login_label.grid(row=0, column=0, pady=15)

    logo_img = ImageTk.PhotoImage(Image.open(
        "resources/logo.jpg").resize((100, 100)))
    logo_label = Label(frame, image=logo_img)
    logo_label.grid(row=1, column=0, pady=10)

    instamed_label = Label(frame, text="Instamed",
                           font=("Arial", 15, "bold"), bg=BG, fg="#551A8B")
    instamed_label.grid(row=2, column=0, pady=10)

    login_labelframe = LabelFrame(frame, text="Login Information", bg=BG)
    login_labelframe.grid(row=3, column=0, padx=20, pady=10)

    username_label = Label(login_labelframe, text="Username", bg=BG)
    username_label.grid(row=0, column=0)

    password_label = Label(login_labelframe, text="Password", bg=BG)
    password_label.grid(row=1, column=0)

    username_entry = Entry(login_labelframe)
    password_entry = Entry(login_labelframe)
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)
    password_entry.config(show="*")  # shows ** when entering password

    for widget in login_labelframe.winfo_children():
        widget.grid_configure(padx=10, pady=10)

    def signin():
        username = username_entry.get()
        password = password_entry.get()

        if username and password:
            if username == "admin" and password == "admin":
                messagebox.showinfo(
                    title="Information", message="Logged into the system.")
                window.destroy()
                import dashboard

            else:
                messagebox.showerror(
                    title="Error", message="Invalid credentials.")

        else:
            messagebox.showwarning(
                title="Warning", message="First name and last name are required.")

    signin_frame = Frame(window, bg=BG)
    signin_frame.grid(row=1, column=0)

    remember_var = tkinter.StringVar(value="Don't Remember")
    terms_check = tkinter.Checkbutton(signin_frame, text="Remember Me",
                                      variable=remember_var, onvalue=True, offvalue=False, bg=BG)
    terms_check.grid(row=0, column=0, pady=10)

    signin_button = tkinter.Button(signin_frame, text="Sign In",
                                   command=signin, bg=BG)
    signin_button.grid(row=0, column=1, sticky="news", padx=30, pady=10)

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()
