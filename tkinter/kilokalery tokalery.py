from  tkinter import *

window= Tk()
window.resizable(0,0)
window.title("Kcal")
window.config(background="red")

def kcal_to_cal():
    kal= entry1.get()
    answer = int(kal) / 1000
    entry2.insert(0,answer)




entry1 = Entry(window, relief=SUNKEN)
entry1.grid(row=0, column=0,  columnspan=2 ,ipady=10, ipadx=32)
for i in range(3):
    lbl = Label(window, text=f"{" " * 15}", fg="red", bg="red").grid()

button = Button(window, text="Convert", padx=30, pady=20,command=kcal_to_cal).grid(row=4 , column=0)
for i in range(3):
    lbl = Label(window, text=f"{" " * 7}", fg="red", bg="red").grid()

tik=IntVar()
btn = Checkbutton(window , text="chek" , variable=tik).grid()

entry2 = Entry(window, relief=SUNKEN)
entry2.grid(ipady=10, ipadx=32)





window.mainloop()