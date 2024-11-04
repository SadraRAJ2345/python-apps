from tkinter import *


window = Tk()

courses = [
    "Python",
    "Javascript",
    "Machine Learning",
    "C++",
    "Dart"
]


selected_option = StringVar()
selected_option.set(courses[0])

OptionMenu(window, selected_option,*courses).grid(padx=30, pady=20)



window.mainloop()