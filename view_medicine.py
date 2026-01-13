from tkinter import *
import sqlite3
from tkinter import ttk
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
    text="Medical Management System - View Medicine",
    font=("Arial", 20, "bold"),
    fg="blue",
    bg="white"
)
HeadingLabel.pack()

# ------------------ MIDDLE FRAME ------------------
MidFrame = Frame(window, width=600, bd=1, bg="white")
MidFrame.pack(side=TOP, pady=10)

# ------------------ VIEW FRAME ------------------
view_frame = Frame(window, width=800, bd=1, bg="white")
view_frame.pack(side=TOP, fill=BOTH, expand=True)

# ------------------ TREEVIEW ------------------
tv = ttk.Treeview(
    view_frame,
    columns=('MedicineName', 'MedicineID', 'Brand', 'ChemicalComponent', 'MFG_Date', 'EXP_Date', 'Price'),
)
# Headings
tv.heading('#0', text='')  # hide first column
tv.heading('#1', text='Medicine Name')
tv.heading('#2', text='Medicine ID')
tv.heading('#3', text='Brand')
tv.heading('#4', text='Chemical Component')
tv.heading('#5', text='MFG Date')
tv.heading('#6', text='EXP Date')
tv.heading('#7', text='Price')

# Columns widths
tv.column('#0', width=0, stretch=NO)
tv.column('#1', width=120)
tv.column('#2', width=100)
tv.column('#3', width=100)
tv.column('#4', width=150)
tv.column('#5', width=100)
tv.column('#6', width=100)
tv.column('#7', width=80)

tv.pack(fill=BOTH, expand=True)

# ------------------ VIEW FUNCTION ------------------


conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()

        # create table if not exists
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

cursor.execute("SELECT * FROM medicine")
data = cursor.fetchall()
for row in data:
    tv.insert('', 'end', values=row)
conn.commit()

def back():
    """Go back to home screen"""
    window.destroy()
    import home  # make sure you have a home.py

# ------------------ BUTTONS ------------------
back_btn = Button(MidFrame, text="Back", font=("Arial", 18, "bold"),
                  fg="white", bg="green", width=15, command=back)
back_btn.grid(row=0, column=0, pady=15)
# ------------------ MAIN LOOP ------------------
window.mainloop()
