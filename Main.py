import tkinter as tk
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
import PIL
import Add_new_face
import Attendacne_taker
import Attendancedata


window = Tk()
window.title("Face recognizer")
window.geometry("1300x720")
window.configure(background="white")



PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47),PIL.Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)

titl = tk.Label(
    window, text="Park college of engineering and technology", bg="black", fg="green", font=("arial", 27),
)
titl.place(x=300, y=12)

a = tk.Label(
    window,
    text="AI Face Attendance System",
    bg="white",
    fg="black",
    bd=10,
    font=("arial", 35),
)
a.pack()

ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=990, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=550, y=270)


def TakeImageUI():
    Add_new_face.main()
    
    
r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=100, y=520)


def automatic_attedance():
    Attendacne_taker.main()


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=550, y=520)


def view_attendance():
    Attendancedata.showAttendance()


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=1000, y=520)

window.mainloop()
