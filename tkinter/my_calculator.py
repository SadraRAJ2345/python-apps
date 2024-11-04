from tkinter import *
root=Tk()

clentry = Entry(width=50)
clentry.grid(row=0,column=0,columnspan=4,ipady=35)


def clear(): 
    mohtava = str(clentry.get())[0:-1]
    clentry.delete(0 ,END)
    clentry.insert(0,mohtava)


def add_number_entry(first_number):
    CURRENT_number=clentry.get()
    clentry.delete(0,END)
    chasb= str(CURRENT_number) + str(first_number)
    clentry.insert(0,chasb)


def add_f():
    global first_number
    global operation
    operation = "add"
    first_number = clentry.get()
    clentry.delete(0 ,END)


def zarb():
    global first_number
    global operation
    operation = "zarb"
    first_number = clentry.get()
    clentry.delete(0 ,END)


def taghsim():
    global first_number
    global operation
    operation = "taghsim"
    first_number = clentry.get()
    clentry.delete(0 ,END)



def tafrigh(): 
    global first_number
    global operation
    operation = "tafrigh"
    first_number = clentry.get()
    clentry.delete(0 ,END)
    

def result():
    global second_number
    second_number = clentry.get()
    clentry.delete(0 , END)
    if operation == "add":
         result = int(first_number) + int(second_number)
    elif operation == "zarb":
         result = int(first_number) * int(second_number)
    elif operation == "taghsim":
         result = int(first_number) / int(second_number)
    else:
         result = int(first_number) - int(second_number)
   
    clentry.insert(0 , result)



btn0=Button(root,text="0",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(0)).grid(row=1,column=0,)
btn1=Button(root,text="1",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(1)).grid(row=1,column=1,)
btn2=Button(root,text="2",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(2)).grid(row=1,column=2,)

btn3=Button(root,text="3",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(3)).grid(row=2,column=0,)
btn4=Button(root,text="4",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(4)).grid(row=2,column=1,)
btn5=Button(root,text="5",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(5)).grid(row=2,column=2,)

btn6=Button(root,text="6",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(6)).grid(row=3,column=0,)
btn7=Button(root,text="7",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(7)).grid(row=3,column=1)
btn8=Button(root,text="8",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(8)).grid(row=3,column=2)

btn9=Button(root,text="9",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=lambda:add_number_entry(9)).grid(row=4,column=0)
btn_clear=Button(root,text="clear",padx=58,pady=25, command=clear).grid(row=4,column=1,columnspan=2)

btn_add = Button(root,text="+",padx=31,pady=25,bg="#000000",fg="#FFFFFF",command=add_f).grid(row=1,column=3)
btn_taghsim = Button(root,text="%",padx=30,pady=25,bg="#000000",fg="#FFFFFF",command=taghsim).grid(row=2,column=3)
btn_zarb =Button(root,text="x",padx=32,pady=25,bg="#000000",fg="#FFFFFF",command=zarb).grid(row=3,column=3)
btn_tafrigh = Button(root,text="-",padx=32,pady=25,bg="#000000",fg="#FFFFFF",command=tafrigh).grid(row=4,column=3)

btn_natige=Button(root,text="=" , padx=145 , pady=40,bg="#000000",fg="#FFFFFF",command=result).grid(row=5,column=0,columnspan=4)



root.mainloop()