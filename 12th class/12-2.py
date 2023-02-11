# from tkinter import *
# from tkinter.filedialog import askopenfilename, asksaveasfilename
# import os

# # define function
# def new_file_func():
#     global file
#     window.title("Untitled - Notepad")
#     file = None
#     Text_Area.delete(1.0, END)

# def open_file_func():
#     global file
#     file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
#     if file == "":
#         file = None
#     else:
#         window.title(os.path.basename(file) + " - Notepad")
#         Text_Area.delete(1.0, END)
#         f = open(file, "r")
#         Text_Area.insert(1.0, f.read())
#         f.close()

# def save_file_func():
#     global file
#     if file == None:
#         file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
#         if file == "":
#             file = None
#         else:
#             f = open(file, "w")
#             f.write(Text_Area.get(1.0, END))
#             f.close()
#             window.title(os.path.basename(file) + " - Notepad")
#             print("File Saved")
#     else:
#         f = open(file, "w")
#         f.write(Text_Area.get(1.0, END))
#         f.close()

# def quit_app_func():
#     window.quit()

# def cut_func():
#     Text_Area.event_generate("<<Cut>>")

# def copy_func():
#     Text_Area.event_generate("<<Copy>>")

# def paste_func():
#     Text_Area.event_generate("<<Paste>>")

# # basic tkinter window setup
# window = Tk()
# window.title("Untitled - Notepad")
# window.geometry("600x700")

# # add text widget
# default_font = ['Times', 20, 'normal']
# Text_Area = Text(window, font=default_font)
# file = None
# Text_Area.pack(expand=True, fill=BOTH)

# # create a menubar
# Menu_Bar = Menu(window)

# # create a file menu
# File_Menu = Menu(Menu_Bar, tearoff=0)
# File_Menu.add_command(label="New", command=new_file_func)
# File_Menu.add_command(label="Open", command=open_file_func)
# File_Menu.add_command(label="Save", command=save_file_func)
# File_Menu.add_separator()
# File_Menu.add_command(label="Exit", command=quit_app_func)

# # create a edit menu
# Edit_Menu = Menu(Menu_Bar, tearoff=0)
# Edit_Menu.add_command(label="Cut", command=cut_func)
# Edit_Menu.add_command(label="Copy", command=copy_func)
# Edit_Menu.add_command(label="Paste", command=paste_func)
# Edit_Menu.add_separator()

# # config a menubar
# Menu_Bar.add_cascade(label="File", menu=File_Menu)
# Menu_Bar.add_cascade(label="Edit", menu=Edit_Menu)
# window.config(menu=Menu_Bar)

# # running window
# window.mainloop()

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# define function
def new_file_func():
    global file
    window.title("Untitled - Notepad")
    file = None
    Text_Area.delete(1.0, END)

def open_file_func():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " - Notepad")
        Text_Area.delete(1.0, END)
        f = open(file, "r")
        Text_Area.insert(1.0, f.read())
        f.close()

def save_file_func():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(Text_Area.get(1.0, END))
            f.close()
            window.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(Text_Area.get(1.0, END))
        f.close()

def quit_app_func():
    window.quit()

def cut_func():
    Text_Area.event_generate("<<Cut>>")

def copy_func():
    Text_Area.event_generate("<<Copy>>")

def paste_func():
    Text_Area.event_generate("<<Paste>>")

# basic tkinter window setup
window = Tk()
window.title("Untitled - Notepad")
window.geometry("600x700")

# add text widget
default_font = ['Times', 20, 'normal']
Text_Area = Text(window, font=default_font)
file = None
Text_Area.pack(expand=True, fill=BOTH)

# create a menubar
Menu_Bar = Menu(window)

# create a file menu
File_Menu = Menu(Menu_Bar, tearoff=0)
File_Menu.add_command(label="New", command=new_file_func)
File_Menu.add_command(label="Open", command=open_file_func)
File_Menu.add_command(label="Save", command=save_file_func)
File_Menu.add_separator()
File_Menu.add_command(label="Exit", command=quit_app_func)

# create a edit menu
Edit_Menu = Menu(Menu_Bar, tearoff=0)
Edit_Menu.add_command(label="Cut", command=cut_func)
Edit_Menu.add_command(label="Copy", command=copy_func)
Edit_Menu.add_command(label="Paste", command=paste_func)
Edit_Menu.add_separator()

# config a menubar
Menu_Bar.add_cascade(label="File", menu=File_Menu)
Menu_Bar.add_cascade(label="Edit", menu=Edit_Menu)
window.config(menu=Menu_Bar)

# running window
window.mainloop()