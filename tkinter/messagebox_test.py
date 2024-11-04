from tkinter import *
from tkinter import messagebox

window = Tk()

def raisee():
    answer = messagebox.askquestion("Something Happened", "صدرا جان استادت خیلی ادم خفنی است درست میگم؟")
    if answer == "no":
        raisee()
    else:
        lbl = Label(window, text="افرین بچه ی خوب").grid()

button = Button(window, text="See Message", padx=40 , pady=30, bg="red", command=raisee).grid(row=0, column=0)



window.mainloop()