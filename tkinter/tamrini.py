from tkinter import *

root = Tk()


entry=Entry(root,width=45)
entry.grid(row=0,column=0)

def label_maker():
        lbl = Label(root, text=f"You have written {entry.get()}").grid()
  


btn=Button(root,text="click hear",command=label_maker)
btn.grid(row=2,column=6)





root.mainloop()