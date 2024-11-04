from tkinter import *

window = Tk()

entry = Entry(width=51,border=5)
entry.grid(row=0, column=0 , columnspan=4, ipady=20)

# functions
def clear_entry():
    entry.delete(0,END)


def add_number_entry(first_name):
    current_number = entry.get()
    entry.delete(0 , END)
    new_value = str(current_number) + str(first_name)
    entry.insert(0 , new_value)
    
def add_f():
    global first_name
    global operation
    operation = "add"
    first_name = entry.get()
    entry.delete(0 ,END)

def multi_f():
    global first_name
    global operation
    operation = "mul"
    first_name = entry.get()
    entry.delete(0 ,END)


def div_f():
    global first_name
    global operation
    operation = "div"
    first_name = entry.get()
    entry.delete(0 ,END)

def sub_f():
    global first_name
    global operation
    operation = "sub"
    first_name = entry.get()
    entry.delete(0 ,END)

def result():
    global second_number
    second_name = entry.get()
    entry.delete(0 , END)
    if operation == "add":
        result = int(first_name) + int(second_name)
    elif operation == "mul":
        result = int(first_name) * int(second_name)
    elif operation == "sub":
        result = int(first_name) - int(second_name)
    else:
        result = int(first_name) / int(second_name)
    entry.insert(0 , result)


# buttons 
button0 = Button(window, text="0", padx=31, pady=25,bg="#8CA5F2",command= lambda: add_number_entry(0))
button1 = Button(window, text="1", padx=30, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(1))
button2 = Button(window, text="2", padx=33, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(2))
button3 = Button(window, text="3", padx=31, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(3))

button4 = Button(window, text="4", padx=31, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(4))
button5 = Button(window, text="5", padx=30, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(5))
button6 = Button(window, text="6", padx=32, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(6))
button7 = Button(window, text="7", padx=32, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(7))

button8 = Button(window, text="8", padx=31, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(8))
button9 = Button(window, text="9", padx=30, pady=25,bg="#8CA5F2",command=lambda:add_number_entry(9))
button_clear = Button(window, text="clear", padx=61, pady=25,bg="#F98D67", command=clear_entry)
button_equal = Button(window, text="Equal", padx=137, pady=30,bg="#F98D67",command=result)

button_add = Button(window, text="+", padx=30, pady=25,bg="#F98D67",command=add_f)
button_subtract = Button(window, text="-", padx=32, pady=25,bg="#F98D67",command=sub_f)
button_division = Button(window, text="%", padx=28, pady=25,bg="#F98D67",command=div_f)
button_multipication = Button(window, text="x", padx=32, pady=25,bg="#F98D67",command=multi_f)

# grid elements
button0.grid(row=1, column=0)
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=2, column=3)

button8.grid(row=3, column=0)
button9.grid(row=3, column=1)
button_clear.grid(row=3, column=2, columnspan=2)

button_add.grid(row=4, column=0)
button_division.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multipication.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=4)

window.mainloop()