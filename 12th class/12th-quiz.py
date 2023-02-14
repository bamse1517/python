# 문제
# from tkinter import *

# # define function
# def new_file_func():
#   pass


# # basic tkinter window setup
# window = Tk()
# window.title("Notepad")
# window.geometry("600x700")

# file = None

# # add text widget
# Text_Area = Text(window, font="lucida 16")
# Text_Area.pack(expand=True, fill=BOTH)

# # create a menubar
# Menu_Bar = Menu(window)

# # create a file menu
# File_Menu = Menu(Menu_Bar, tearoff=0)
# File_Menu.add_command(label="New", command=new_file_func)

# # running window
# window.mainloop()


# 답
from tkinter import *

# define function
def new_file_func():
  pass

# basic tkinter window setup
window = Tk()
window.title("Notepad")
window.geometry("600x700")

file = None

# add text widget
Text_Area = Text(window, font="lucida 16")
Text_Area.pack(expand=True, fill=BOTH)

# create a menubar
Menu_Bar = Menu(window)

# create a file menu
File_Menu = Menu(Menu_Bar, tearoff=0)
File_Menu.add_command(label="New", command=new_file_func)

# config a menubar
Menu_Bar.add_cascade(label="File", menu=File_Menu)
window.config(menu=Menu_Bar)

# running window
window.mainloop()
