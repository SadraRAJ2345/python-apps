from tkinter import *

window = Tk()

meghdar = IntVar()
meghdar.set(1)
btn = Checkbutton(window,variable=meghdar).grid()



window.mainloop()