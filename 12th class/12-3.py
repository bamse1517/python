# from tkinter import *
# from tkinter.filedialog import askopenfilename, asksaveasfilename
# from tkinter.messagebox import showinfo

# # 이벤트 함수 정의
# def new_file_func():
#   text_area.delete(1.0, END)

# def open_file_func():
#   global file
#   file = askopenfilename()
#   text_area.delete(1.0, END)
#   f = open(file, "r", encoding="UTF8")
#   text_area.insert(1.0, f.read())
#   f.close()

# def save_file_func():
#   global file
#   file = asksaveasfilename()
#   f = open(file, "w", encoding="UTF8")
#   f.write(text_area.get(1.0, END))
#   f.close()

# def quit_app_func():
#   window.quit()

# def cut_func():
#   text_area.event_generate("<<Cut>>")

# def copy_func():
#   text_area.event_generate("<<Copy>>")

# def paste_func():
#   text_area.event_generate("<<Paste>>")

# def about_func():
#   showinfo("Notepad", "Version 0.0.1")

# # 윈도우 생성
# window = Tk()
# window.title("Notepad")
# window.geometry("600x700")

# # 메뉴 생성
# menu_bar = Menu(window)

# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="New", command=new_file_func)
# file_menu.add_command(label="Open", command=open_file_func)
# file_menu.add_command(label="Save", command=save_file_func)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=quit_app_func)

# edit_menu = Menu(menu_bar, tearoff=0)
# edit_menu.add_command(label="Cut", command=cut_func)
# edit_menu.add_command(label="Copy", command=copy_func)
# edit_menu.add_command(label="Paste", command=paste_func)

# help_menu = Menu(menu_bar, tearoff=0)
# help_menu.add_command(label="About", command=about_func)

# menu_bar.add_cascade(label="File", menu=file_menu)
# menu_bar.add_cascade(label="Edit", menu=edit_menu)
# menu_bar.add_cascade(label="Help", menu=help_menu)
# window.config(menu=menu_bar)

# # UI 생성
# text_area = Text(window, font="lucida 16")

# # UI 배치
# text_area.pack(expand=True, fill=BOTH)

# # 윈도우 실행
# window.mainloop()

# from tkinter import *
# from tkinter.filedialog import askopenfilename, asksaveasfilename
# from tkinter.messagebox import showinfo

# # 이벤트 함수 정의
# def new_file_func():
#   text_area.delete(1.0, END)

# def open_file_func():
#   global file
#   file = askopenfilename()
#   text_area.delete(1.0, END)
#   f = open(file, "r", encoding="UTF8")
#   text_area.insert(1.0, f.read())
#   f.close()

# def save_file_func():
#   global file
#   file = asksaveasfilename()
#   f = open(file, "w", encoding="UTF8")
#   f.write(text_area.get(1.0, END))
#   f.close()

# def quit_app_func():
#   window.quit()

# def cut_func():
#   text_area.event_generate("<<Cut>>")

# def copy_func():
#   text_area.event_generate("<<Copy>>")

# def paste_func():
#   text_area.event_generate("<<Paste>>")

# def about_func():
#   showinfo("Notepad", "Version 0.0.1")

# # 윈도우 생성
# window = Tk()
# window.title("Notepad")
# window.geometry("600x700")

# # 메뉴 생성
# menu_bar = Menu(window)

# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="New", command=new_file_func)
# file_menu.add_command(label="Open", command=open_file_func)
# file_menu.add_command(label="Save", command=save_file_func)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=quit_app_func)

# edit_menu = Menu(menu_bar, tearoff=0)
# edit_menu.add_command(label="Cut", command=cut_func)
# edit_menu.add_command(label="Copy", command=copy_func)
# edit_menu.add_command(label="Paste", command=paste_func)

# help_menu = Menu(menu_bar, tearoff=0)
# help_menu.add_command(label="About", command=about_func)

# menu_bar.add_cascade(label="File", menu=file_menu)
# menu_bar.add_cascade(label="Edit", menu=edit_menu)
# menu_bar.add_cascade(label="Help", menu=help_menu)
# window.config(menu=menu_bar)

# # UI 생성
# text_area = Text(window, font="lucida 16")
# text_scroll = Scrollbar(text_area)
# text_scroll.config(command=text_area.yview)
# text_area.config(yscrollcommand=text_scroll.set)

# # UI 배치
# text_area.pack(expand=True, fill=BOTH)
# text_scroll.pack(side=RIGHT, fill=Y)

# # 윈도우 실행
# window.mainloop()

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

# 이벤트 함수 정의
def new_file_func():
  text_area.delete(1.0, END)

def open_file_func():
  global file
  file = askopenfilename()
  text_area.delete(1.0, END)
  f = open(file, "r", encoding="UTF8")
  text_area.insert(1.0, f.read())
  f.close()

def save_file_func():
  global file
  file = asksaveasfilename()
  f = open(file, "w", encoding="UTF8")
  f.write(text_area.get(1.0, END))
  f.close()

def quit_app_func():
  window.quit()

def cut_func():
  text_area.event_generate("<<Cut>>")

def copy_func():
  text_area.event_generate("<<Copy>>")

def paste_func():
  text_area.event_generate("<<Paste>>")

def about_func():
  showinfo("Notepad", "Version 0.0.1")

def font_size_up_func():
  default_font[1] = default_font[1] + 5
  text_area.config(font=default_font)

def font_size_down_func():
  default_font[1] = default_font[1] - 5
  text_area.config(font=default_font)


# 윈도우 생성
window = Tk()
window.title("Notepad")
window.geometry("600x700")

# 메뉴 생성
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file_func)
file_menu.add_command(label="Open", command=open_file_func)
file_menu.add_command(label="Save", command=save_file_func)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app_func)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_func)
edit_menu.add_command(label="Copy", command=copy_func)
edit_menu.add_command(label="Paste", command=paste_func)
edit_menu.add_separator()

font_menu = Menu(edit_menu, tearoff=0)
font_menu.add_command(label="Up + ", command=font_size_up_func)
font_menu.add_command(label="Down - ", command=font_size_down_func)

edit_menu.add_cascade(label="Font Size", menu=font_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about_func)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)
window.config(menu=menu_bar)

# UI 생성
default_font = ["lucida", 30]
text_area = Text(window, font=default_font)
text_scroll = Scrollbar(text_area)
text_scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=text_scroll.set)

# UI 배치
text_area.pack(expand=True, fill=BOTH)
text_scroll.pack(side=RIGHT, fill=Y)

# 윈도우 실행
window.mainloop()