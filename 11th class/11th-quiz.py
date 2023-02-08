# # 문제
# from tkinter import *

# def btn_func():
#     label.configure(text="button click!")

# window = Tk()
# label = Label(window)
# btn = Button(window, text="Click")
# btn.pack()

# window.mainloop()

# 답
from tkinter import *

def btn_func():
    label.configure(text="button click!")

window = Tk()

label = Label(window)
btn = Button(window, text="Click", command=btn_func)

label.pack()
btn.pack()

window.mainloop()
