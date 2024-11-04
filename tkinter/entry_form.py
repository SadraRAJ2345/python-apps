from tkinter import *

window = Tk()
def submit_data():
    fn = entry1.get()
    entry1.delete(0 , END)
    ln = entry2.get()
    entry2.delete(0 , END)
    ad = entry5.get()
    entry3.delete(0 , END)
    ag = entry4.get()
    entry4.delete(0 , END)
    idn = entry3.get()
    entry5.delete(0 , END)

    final_label = Label(window, text="Data has been collected succesfully.").grid()

entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)
entry4 = Entry(window)
entry5 = Entry(window)

lbl1 = Label(window, text="First Name")
lbl2 = Label(window, text="Last Name")
lbl3 = Label(window, text="Idenity Card")
lbl4 = Label(window, text="Age")
lbl5 = Label(window, text="Address")

submit_button = Button(window, text="Submit", padx=20, pady=10, bg="green", command=submit_data).grid(row=5,column=1)
defaullt = IntVar()
Checkbutton(window, text="Privacy Policy", variable=defaullt).grid()



lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
lbl3.grid(row=2, column=0)
lbl4.grid(row=3, column=0)
lbl5.grid(row=4, column=0)

entry1.grid(row=0 , column=1)
entry2.grid(row=1 , column=1)
entry3.grid(row=2 , column=1)
entry4.grid(row=3 , column=1)
entry5.grid(row=4 , column=1)

window.mainloop()