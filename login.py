from tkinter import *
import sqlite3
import tkinter.messagebox as msg

# ------------------ MAIN WINDOW ------------------
window = Tk()
window.geometry("900x600")
window.title("Medical Management System")

# ------------------ VARIABLES ------------------
username_var = StringVar()
password_var = StringVar()

# ------------------ FUNCTIONS ------------------
def login():
    """Validate login credentials from SQLite"""
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM userdata
        WHERE Username=? AND Password=?
    """, (
        username_var.get(),
        password_var.get()
    ))

    result = cursor.fetchone()
    conn.close()

    if result:
        msg.showinfo("Login Successful", f"Welcome, {username_var.get()}!", icon="info")
        window.destroy()
        import home
    else:
        msg.showerror("Error", "Invalid Username or Password", icon="error")



def go_to_register():
    """Open the register window"""
    window.destroy()
    import register  # make sure register.py exists


# ------------------ BACKGROUND IMAGE ------------------
reg_image = PhotoImage(file="medd.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------ TOP HEADING ------------------
TopHeadingFrame = Frame(window, width=700, bd=1, bg="white")
TopHeadingFrame.pack(side=TOP, pady=20)

HeadingLabel = Label(
    TopHeadingFrame,
    text="Medical Management System - Login",
    font=("Arial", 20, "bold"),
    fg="blue",
    bg="white"
)
HeadingLabel.pack()

# ------------------ MIDDLE FRAME ------------------
MidFrame = Frame(window, width=600, bd=1, bg="white")
MidFrame.pack(pady=30)

# ------------------ FORM FIELDS ------------------
Label(MidFrame, text="Username", font=("Arial", 20, "bold"), fg="blue", bg="white").grid(row=0, column=0, padx=10, pady=10)
Entry(MidFrame, font=("Arial", 20), textvariable=username_var).grid(row=0, column=1, padx=10, pady=10)

Label(MidFrame, text="Password", font=("Arial", 20, "bold"), fg="blue", bg="white").grid(row=1, column=0, padx=10, pady=10)
Entry(MidFrame, font=("Arial", 20), textvariable=password_var, show="*").grid(row=1, column=1, padx=10, pady=10)

# ------------------ BUTTONS ------------------
Login_btn = Button(
    MidFrame,
    text="Login",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="green",
    width=10,
    command=login
)
Login_btn.grid(row=2, column=1, pady=15)

Register_btn = Button(
    MidFrame,
    text="Register",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="blue",
    width=10,
    command=go_to_register
)
Register_btn.grid(row=3, column=1, pady=10)

# Optional clickable label
NotUserLabel = Label(
    MidFrame,
    text="New user? Click Register",
    font=("Arial", 14, "bold"),
    fg="blue",
    bg="white",
    cursor="hand2"
)
NotUserLabel.grid(row=3, column=0, pady=10)
NotUserLabel.bind("<Button-1>", lambda e: go_to_register())

# ------------------ MAIN LOOP ------------------
window.mainloop()
