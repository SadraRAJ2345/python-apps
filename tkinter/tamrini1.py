from tkinter import *

window = Tk()
window.title("برنامه مورد نیاز")
window.resizable(True , False)
def hichi():
    lbl=Label (window , text=f"you have written:{clentry.get()})").grid()



lbl1 = Label(window,text="im sadra im very biutifull")
lbl2 = Label(window,text="sadra is man")
lbl1.grid(row=2,column=2)
lbl2.grid(row=0,column=0)


clentry = Entry(window,width=50)
clentry.grid(row=1,column=2,columnspan=3)


btn = Button(window,text="click here", command=hichi, padx=30 ,bg="#54FCDB", fg="black")

btn.grid(row=6,column=4)

window.mainloop()