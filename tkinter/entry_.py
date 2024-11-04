from tkinter import *

window = Tk()


def handle_request():
    lbl = Label(window, text=f"You have written {prentry.get()}").grid()

prentry = Entry(window, width=50)
btn = Button(window,text="send", padx=30, pady=20, command=handle_request,bg="gray")

btn.grid(row=1 , column=0)
prentry.grid(row=0, column=0)




window.mainloop()