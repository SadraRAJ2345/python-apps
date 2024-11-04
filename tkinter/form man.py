from tkinter import *


root=Tk()
root.resizable(0,0)

def sub():
    
    fn = clentry1.get()
    clentry1.delete(0 , END)
    ln = clentry2.get()
    clentry2.delete(0 , END)
    ad = clentry5.get()
    clentry3.delete(0 , END)
    ag = clentry4.get()
    clentry4.delete(0 , END)
    idn = clentry3.get()
    clentry5.delete(0 , END)
    datas = [fn,ln,ad,ag,idn]
    for i in datas:
        if i == "":
            final_label = Label(root, text="Don't leave a field blank").grid()
            break
    else:
        final_label = Label(root, text="Data has been collected succesfully.").grid()



clentry1=Entry(root)
clentry2=Entry(root)
clentry3=Entry(root)
clentry4=Entry(root)
clentry5=Entry(root)


btn = Button(root , text="tayid" , padx=20 , pady=12 , bg="black",command=sub).grid(row=5 , column=1)

clentry1.grid(row=0 , column=1)
clentry2.grid(row=1, column=1)
clentry3.grid(row=2 , column=1)
clentry4.grid(row=3 , column=1)
clentry5.grid(row=4 , column=1)






lbl0=Label(root , text="first name" )
lbl1=Label(root , text="last name" )
lbl2=Label(root , text="kode meli" )
lbl3=Label(root , text="kode posti" )
lbl4=Label(root , text=" shomare mamanet" )


chek = IntVar()
Checkbutton(root , text="bede bere",variable=chek).grid()


lbl0.grid(row=0, column=0)
lbl1.grid(row=1,column=0)
lbl2.grid(row=2 , column=0)
lbl3.grid(row=3 , column=0)
lbl4.grid(row=4 , column=0)



root.mainloop()





