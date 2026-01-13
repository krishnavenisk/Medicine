from tkinter import *
import sqlite3

# ------------------ MAIN WINDOW ------------------
window = Tk()
window.geometry("900x600")
window.title("Medical Management System")
window.iconbitmap("icon.ico")

# ------------------ BACKGROUND IMAGE ------------------
reg_image = PhotoImage(file="medd.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------ TOP HEADING ------------------
TopHeadingFrame = Frame(window, width=700, bd=1, bg="white")
TopHeadingFrame.pack(side=TOP, pady=20)

HeadingLabel = Label(
    TopHeadingFrame,
    text="Medical Management System - Home",
    font=("Arial", 20, "bold"),
    fg="blue",
    bg="white"
)
HeadingLabel.pack()

# ------------------ MIDDLE FRAME ------------------
MidFrame = Frame(window, width=600, bd=1, bg="white")
MidFrame.pack(pady=30)

# ------------------ FUNCTIONS ------------------
def add():
    window.destroy()
    import add_medicine

def view():
    window.destroy()
    import view_medicine

def search():
    window.destroy()
    import search_medicine

def delete():
    window.destroy()
    import delete_medicine

def logout():
    window.destroy()
    import login

# ------------------ BUTTONS ------------------
add_btn = Button(
    MidFrame,
    text="Add MEDICINE",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="green",
    width=20,
    command=add
)
add_btn.grid(row=0, column=0, pady=15, padx=20)

view_btn = Button(
    MidFrame,
    text="View MEDICINE",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="green",
    width=20,
    command=view
)
view_btn.grid(row=1, column=0, pady=15, padx=20)

search_btn = Button(
    MidFrame,
    text="Search MEDICINE",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="green",
    width=20,
    command=search
)
search_btn.grid(row=2, column=0, pady=15, padx=20)

delete_btn = Button(
    MidFrame,
    text="Delete MEDICINE",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="green",
    width=20,
    command=delete
)
delete_btn.grid(row=3, column=0, pady=15, padx=20)

logout_btn = Button(
    MidFrame,
    text="Logout",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="red",
    width=20,
    command=logout
)
logout_btn.grid(row=4, column=0, pady=15, padx=20)

# ------------------ MAIN LOOP ------------------
window.mainloop()
