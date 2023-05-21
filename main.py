import ttkbootstrap as ttk
from ttkbootstrap.dialogs.dialogs import Messagebox
from PIL import ImageTk, Image

DATABASE_NAME = "warehouse2"
PASSWORD = "murtu"
THEME = "cyborg"
FONT_NAME = "Cascadia Code"


def main():
    window = ttk.Window(themename=THEME, iconphoto=None)
    window.title("Login")

    window.style.configure('.', font=(FONT_NAME, 15))

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0)

    login_label = ttk.Label(frame, text="LOGIN", font=(
        FONT_NAME, 25, "bold"))
    login_label.grid(row=0, column=0, pady=15)

    logo_img = ImageTk.PhotoImage(Image.open(
        "logo.jpg").resize((100, 100)))
    logo_label = ttk.Label(frame, image=logo_img)
    logo_label.grid(row=1, column=0, pady=10)

    instamed_label = ttk.Label(frame, text="Instamed",
                               font=(FONT_NAME, 18, "bold"))
    instamed_label.grid(row=2, column=0, pady=10)

    login_labelframe = ttk.LabelFrame(frame, text="Login Information")
    login_labelframe.grid(row=3, column=0, padx=20, pady=10)

    username_label = ttk.Label(login_labelframe, text="Username")
    username_label.grid(row=0, column=0)

    password_label = ttk.Label(login_labelframe, text="Password")
    password_label.grid(row=1, column=0)

    username_entry = ttk.Entry(login_labelframe)
    password_entry = ttk.Entry(login_labelframe)
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)
    password_entry.config(show="•")  # shows ** when entering password

    for widget in login_labelframe.winfo_children():
        widget.grid_configure(padx=10, pady=10)

    def signin():
        username = username_entry.get()
        password = password_entry.get()

        if username and password:
            if username == "admin" and password == "admin":
                Messagebox.show_info(
                    title="Information", message="Logged into the system.")

                # window.withdraw()
                import dashboard
                dashboard.start(window)

            else:
                Messagebox.show_error(
                    title="Error", message="Invalid credentials.")

        else:
            Messagebox.show_warning(
                title="Warning", message="Username and password are required.")

    signin_frame = ttk.Frame(window)
    signin_frame.grid(row=1, column=0)

    signin_button = ttk.Button(signin_frame, text="Sign In",
                               command=signin)
    signin_button.grid(row=0, column=1, sticky="news", padx=30, pady=10)

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()
