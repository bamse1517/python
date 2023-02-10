# from tkinter import *

# # 윈도우 생성
# window = Tk()
# window.title("Notepad")
# window.geometry("600x700")

# # UI 생성
# text_area = Text(window, font="lucida 16")

# # UI 배치
# text_area.pack(expand=True, fill=BOTH)

# # 윈도우 실행
# window.mainloop()

# from tkinter import *

# # define function
# def new_file_func():
#     pass

# def open_file_func():
#     pass

# def save_file_func():
#     pass

# def quit_app_func():
#     pass

# # basic tkinter window setup
# window = Tk()
# window.title("Notepad")
# window.geometry("600x700")

# # add text widget
# Text_Area = Text(window, font="lucida 16")
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

# # config a menubar
# Menu_Bar.add_cascade(label="File", menu=File_Menu)
# window.config(menu=Menu_Bar)

# # running window
# window.mainloop()

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

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

menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# UI 생성
text_area = Text(window, font="lucida 16")

# UI 배치
text_area.pack(expand=True, fill=BOTH)

# 윈도우 실행
window.mainloop()