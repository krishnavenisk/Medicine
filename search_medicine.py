from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox as msg

# ------------------ MAIN WINDOW ------------------
window = Tk()
window.geometry("900x600")
window.title("Medical Management System")

# ------------------ BACKGROUND IMAGE ------------------
reg_image = PhotoImage(file="medd.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------ TOP HEADING ------------------
TopHeadingFrame = Frame(window, width=700, bd=1, bg="white")
TopHeadingFrame.pack(side=TOP, pady=20)

HeadingLabel = Label(
    TopHeadingFrame,
    text="Medical Management System - Search Medicine",
    font=("Arial", 20, "bold"),
    fg="blue",
    bg="white"
)
HeadingLabel.pack()

# ------------------ SEARCH FRAME ------------------
SearchFrame = Frame(window, bg="white")
SearchFrame.pack(pady=10)

Label(SearchFrame, text="Medicine Name:", font=("Arial", 14), bg="white").grid(row=0, column=0, padx=10)
search_var = StringVar()
search_entry = Entry(SearchFrame, textvariable=search_var, font=("Arial", 14), width=25)
search_entry.grid(row=0, column=1, padx=10)

search_btn = Button(
    SearchFrame,
    text="Search",
    font=("Arial", 14, "bold"),
    bg="blue",
    fg="white",
    width=10,
    command=lambda: search_medicine()
)
search_btn.grid(row=0, column=2, padx=10)

show_all_btn = Button(
    SearchFrame,
    text="Show All",
    font=("Arial", 14, "bold"),
    bg="gray",
    fg="white",
    width=10,
    command=lambda: load_data()
)
show_all_btn.grid(row=0, column=3, padx=10)

# ------------------ VIEW FRAME ------------------
view_frame = Frame(window, bg="white")
view_frame.pack(fill=BOTH, expand=True, pady=10)

# ------------------ TREEVIEW ------------------
tv = ttk.Treeview(
    view_frame,
    columns=('MedicineID', 'MedicineName', 'Brand', 'ChemicalComponent', 'MFG_Date', 'EXP_Date', 'Price'),
    show='headings'
)

# Headings
for col in tv["columns"]:
    tv.heading(col, text=col.replace("_", " "))

# Column widths
tv.column('MedicineID', width=100)
tv.column('MedicineName', width=150)
tv.column('Brand', width=120)
tv.column('ChemicalComponent', width=160)
tv.column('MFG_Date', width=100)
tv.column('EXP_Date', width=100)
tv.column('Price', width=80)

tv.pack(fill=BOTH, expand=True)

# ------------------ DATABASE ------------------
conn = sqlite3.connect('medicine.db')
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

# ------------------ LOAD ALL DATA ------------------
def load_data():
    tv.delete(*tv.get_children())
    cursor.execute("SELECT * FROM medicine")
    rows = cursor.fetchall()
    for row in rows:
        tv.insert('', END, values=row)

# ------------------ SEARCH FUNCTION ------------------
def search_medicine():
    name = search_var.get().strip()

    if name == "":
        msg.showwarning("Warning", "Please enter medicine name")
        return

    tv.delete(*tv.get_children())
    cursor.execute(
        "SELECT * FROM medicine WHERE MedicineName LIKE ?",
        ('%' + name + '%',)
    )
    rows = cursor.fetchall()

    if not rows:
        msg.showinfo("Result", "No medicine found")

    for row in rows:
        tv.insert('', END, values=row)

# Load all records at start
load_data()

# ------------------ BACK BUTTON ------------------
def back():
    window.destroy()
    import home

back_btn = Button(
    window,
    text="Back",
    font=("Arial", 16, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=back
)
back_btn.pack(pady=10)

# ------------------ MAIN LOOP ------------------
window.mainloop()
conn.close()
