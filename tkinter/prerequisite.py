from tkinter import *

# basic setup
window = Tk()
window.title("برنامه اول من")
window.resizable(False,False)
window.config()
# window.geometry("500x350")

# Labels in Tkinter
# lbl_1 = Label(window,text="this is my first tkinter exprience")
# lbl_2 = Label(window, text="this is the second one")

program_entry = Entry(window)
program_entry.grid(row=1,column=2, columnspan=3)

btn1 = Button(window, text="Click Here",padx=90 , pady=18,bg="#54FCDB",fg='white',borderwidth=10)
btn2 = Button(window, text="Click Here",padx=90 , pady=18,bg="green",fg='white',borderwidth=10)
btn3 = Button(window, text="Click Here",padx=90 , pady=18,bg="#54FCDB",fg='white',borderwidth=10)

# where we pack stuff = HEX . htmlcolorcodes.com
btn1.grid(row=0 , column=0)
btn2.grid(row=0 , column=1)
btn3.grid(row=0 , column=2)
# lbl_1.grid(row=0, column=0)
# lbl_2.grid(row=300, column=3)




window.mainloop()