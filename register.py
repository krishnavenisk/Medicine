from tkinter import *
import sqlite3
import tkinter.messagebox as msg

# ------------------ MAIN WINDOW ------------------
window = Tk()
window.geometry("900x600")
window.title("Medical Management System - Register")
window.iconbitmap("icon.ico")

# ------------------ TOP HEADING ------------------
TopHeadingFrame = Frame(window, width=700, bd=1, bg="white")
TopHeadingFrame.pack(side=TOP, pady=20)

HeadingLabel = Label(
    TopHeadingFrame,
    text="Medical Management System - User Registration",
    font=("Arial", 20, "bold"),
    fg="blue",
    bg="white"
)
HeadingLabel.pack()

# ------------------ MIDDLE FRAME ------------------
MidFrame = Frame(window, width=600, bd=1, bg="white")
MidFrame.pack(pady=30)

# ------------------ VARIABLES ------------------
UserID_var = StringVar()
Username_var = StringVar()
Email_var = StringVar()
Password_var = StringVar()
ConfirmPassword_var = StringVar()

# ------------------ DATABASE SETUP ------------------
conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        UserID TEXT PRIMARY KEY,
        Username TEXT,
        Email TEXT,
        Password TEXT
    )
""")
conn.commit()

# ------------------ FUNCTIONS ------------------
def register_user():
    if (
        UserID_var.get() == "" or
        Username_var.get() == "" or
        Email_var.get() == "" or
        Password_var.get() == "" or
        ConfirmPassword_var.get() == ""
    ):
        msg.showwarning("Warning", "All fields are required!")
        return

    if Password_var.get() != ConfirmPassword_var.get():
        msg.showerror("Error", "Passwords do not match!")
        return

    try:
        cursor.execute("""
            INSERT INTO users (UserID, Username, Email, Password)
            VALUES (?, ?, ?, ?)
        """, (
            UserID_var.get(),
            Username_var.get(),
            Email_var.get(),
            Password_var.get()
        ))
        conn.commit()

        msg.showinfo("Success", "Registration successful! Please login.")
        window.destroy()
        import login   # 🔁 REDIRECT TO LOGIN PAGE

    except sqlite3.IntegrityError:
        msg.showerror("Error", "User ID already exists!")

def go_to_login():
    window.destroy()
    import login

# ------------------ LABELS & ENTRY FIELDS ------------------
Label(MidFrame, text="User ID", font=("Arial", 20, "bold"), fg="blue", bg="white")\
    .grid(row=0, column=0, padx=10, pady=10, sticky=W)
Entry(MidFrame, font=("Arial", 20), textvariable=UserID_var)\
    .grid(row=0, column=1, padx=10, pady=10)

Label(MidFrame, text="Username", font=("Arial", 20, "bold"), fg="blue", bg="white")\
    .grid(row=1, column=0, padx=10, pady=10, sticky=W)
Entry(MidFrame, font=("Arial", 20), textvariable=Username_var)\
    .grid(row=1, column=1, padx=10, pady=10)

Label(MidFrame, text="Email", font=("Arial", 20, "bold"), fg="blue", bg="white")\
    .grid(row=2, column=0, padx=10, pady=10, sticky=W)
Entry(MidFrame, font=("Arial", 20), textvariable=Email_var)\
    .grid(row=2, column=1, padx=10, pady=10)

Label(MidFrame, text="Password", font=("Arial", 20, "bold"), fg="blue", bg="white")\
    .grid(row=3, column=0, padx=10, pady=10, sticky=W)
Entry(MidFrame, font=("Arial", 20), textvariable=Password_var, show="*")\
    .grid(row=3, column=1, padx=10, pady=10)

Label(MidFrame, text="Confirm Password", font=("Arial", 20, "bold"), fg="blue", bg="white")\
    .grid(row=4, column=0, padx=10, pady=10, sticky=W)
Entry(MidFrame, font=("Arial", 20), textvariable=ConfirmPassword_var, show="*")\
    .grid(row=4, column=1, padx=10, pady=10)

# ------------------ BUTTONS ------------------
Button(
    MidFrame,
    text="Register",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="green",
    width=15,
    command=register_user
).grid(row=5, column=1, pady=15)

Button(
    MidFrame,
    text="Already have an account? Login",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="blue",
    width=25,
    command=go_to_login
).grid(row=6, column=1, pady=10)

# ------------------ MAIN LOOP ------------------
window.mainloop()
conn.close()
