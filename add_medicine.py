from tkinter import *
import sqlite3
import tkinter.messagebox as msg

# ------------------ MAIN WINDOW ------------------
window = Tk()
window.geometry("900x600")
window.title("Medical Management System")
window.iconbitmap("icon.ico")  # optional icon

# ------------------ BACKGROUND IMAGE ------------------
reg_image = PhotoImage(file="medd.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------ TOP HEADING ------------------
TopHeadingFrame = Frame(window, width=700, bd=1, bg="white")
TopHeadingFrame.pack(side=TOP, pady=20)

HeadingLabel = Label(
    TopHeadingFrame,
    text="Medical Management System - Add Medicine",
    font=("Arial", 20, "bold"),
    fg="blue",
    bg="white"
)
HeadingLabel.pack()

# ------------------ MIDDLE FRAME ------------------
MidFrame = Frame(window, width=600, bd=1, bg="white")
MidFrame.pack(pady=30)

# ------------------ DATABASE SETUP ------------------
conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicine (
        MedicineID TEXT PRIMARY KEY,
        MedicineName TEXT,
        Brand TEXT,
        ChemicalComponent TEXT,
        MFG_Date TEXT,
        EXP_Date TEXT,
        Price TEXT
    )
""")
conn.commit()

# ------------------ VARIABLES ------------------
MedicineID_var = StringVar()
MedicineName_var = StringVar()
Brand_var = StringVar()
ChemicalComponent_var = StringVar()
MFG_Date_var = StringVar()
EXP_Date_var = StringVar()
Price_var = StringVar()  # now all are strings

# ------------------ FUNCTIONS ------------------
def add_medicine():
    """Insert new medicine into the database as strings"""
    if not MedicineID_var.get() or not MedicineName_var.get():
        msg.showwarning("Input Error", "Medicine ID and Name are required")
        return

    try:
        cursor.execute("""
            INSERT INTO medicine (MedicineID, MedicineName, Brand, ChemicalComponent, MFG_Date, EXP_Date, Price)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            str(MedicineID_var.get()),
            str(MedicineName_var.get()),
            str(Brand_var.get()),
            str(ChemicalComponent_var.get()),
            str(MFG_Date_var.get()),
            str(EXP_Date_var.get()),
            str(Price_var.get())
        ))
        conn.commit()
        msg.showinfo("Success", f"Medicine '{MedicineName_var.get()}' added successfully!", icon="info")
        window.destroy()
        import home  # redirect to home screen
    except sqlite3.IntegrityError:
        msg.showerror("Error", "Medicine ID already exists!", icon="error")


def go_to_home():
    """Go back to home screen without adding medicine"""
    window.destroy()
    import home  # redirect to home screen

# ------------------ FORM FIELDS ------------------
fields = [
    ("Medicine ID", MedicineID_var),
    ("Medicine Name", MedicineName_var),
    ("Brand", Brand_var),
    ("Chemical Component", ChemicalComponent_var),
    ("Manufacture Date", MFG_Date_var),
    ("Expiry Date", EXP_Date_var),
    ("Price", Price_var),
]

for idx, field in enumerate(fields):
    Label(MidFrame, text=field[0], font=("Arial", 20, "bold"), fg="blue", bg="white")\
        .grid(row=idx, column=0, padx=10, pady=10)
    Entry(MidFrame, font=("Arial", 20), textvariable=field[1])\
        .grid(row=idx, column=1, padx=10, pady=10)

# ------------------ BUTTONS ------------------
submit_btn = Button(
    MidFrame,
    text="Add Medicine",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="green",
    width=15,
    command=add_medicine
)
submit_btn.grid(row=len(fields), column=1, pady=15)

home_btn = Button(
    MidFrame,
    text="Back to Home",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="blue",
    width=15,
    command=go_to_home
)
home_btn.grid(row=len(fields)+1, column=1, pady=10)

# ------------------ MAIN LOOP ------------------
window.mainloop()
