# # 입력창 만들기
# from tkinter import *

# # 윈도우 생성
# window = Tk()
# window.geometry("500x500")

# # UI 만들기
# name = Entry(window)
# name.pack()

# # 윈도우 실행
# window.mainloop()

# # 입력창에 작성한 텍스트 확인하기
# from tkinter import *

# # 이벤트 함수 정의
# def submit():
#   label.configure(text=name_var.get())

# # 윈도우 생성
# window = Tk()
# window.geometry("500x500")

# # 입력 데이터
# name_var = StringVar()

# # UI 만들기
# name = Entry(window, textvariable=name_var)
# btn = Button(window, text="Submit", command=submit)
# label = Label(window, text="입력창에 텍스트를 작성하고 버튼을 클릭하세요.")

# # UI 배치
# name.pack()
# btn.pack()
# label.pack()

# # 윈도우 실행
# window.mainloop()

# from tkinter import *

# # 이벤트 함수 정의
# def submit():
#   label.configure(text=name_var.get())

# def it_has_been_written(*args):
#   label.configure(text=name_var.get())

# # 윈도우 생성
# window = Tk()
# window.geometry("500x500")

# # 데이터
# name_var = StringVar()
# name_var.trace("w", it_has_been_written)

# # UI 만들기
# name = Entry(window, textvariable=name_var)
# btn = Button(window, text="Submit", command=submit)
# label = Label(window, text="입력창에 텍스트를 작성하고 버튼을 클릭하세요.")

# # UI 배치
# name.pack()
# btn.pack()
# label.pack()

# # 메인루프 실행
# window.mainloop()

# from tkinter import *


# # 이벤트 함수 정의
# def it_has_been_written(*args):
#   output_label.configure(text=name_var.get())

# # 윈도우 생성
# window = Tk()
# window.geometry("300x100")
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)

# # UI 만들기
# Label(window, text="Name:").grid(column=0, row=0, padx=5, pady=5)

# name_var = StringVar()
# name_var.trace("w", it_has_been_written)

# name_entry = Entry(window, textvariable=name_var)
# name_entry.grid(column=1, row=0, padx=5, pady=5)
# name_entry.focus()

# output_label = Label(window)
# output_label.grid(column=0, row=1, columnspan=3, padx=5, pady=5)

# # 윈도우 실행
# window.mainloop()

# from tkinter import *

# # 이벤트 함수 정의
# def submit():
#   label.configure(text=name_var.get())

# def it_has_been_written(*args):
#   if name_var.get() == "":
#     label.configure(text="")
#   else:
#     label.configure(text="typing...")

# # 윈도우 생성
# window = Tk()
# window.geometry("400x100")
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)

# # 데이터
# name_var = StringVar()
# name_var.trace("w", it_has_been_written)

# # UI 만들기
# Label(window, text="Name: ").grid(column=0, row=0, padx=5, pady=5)
# name = Entry(window, textvariable=name_var)
# btn = Button(window, text="Submit", command=submit)
# label = Label(window, text="입력창에 텍스트를 작성하고 버튼을 클릭하세요.")

# # UI 배치
# name.grid(column=1, row=0, padx=5, pady=5)
# btn.grid(column=2, row=0, padx=5, pady=5)
# label.grid(column=1, row=1, padx=5, pady=5)

# # 메인루프 실행
# window.mainloop()


# 두 개의 입력창에 작성한 텍스트 비교하기
from tkinter import *

# 이벤트 함수 정의
def validate(*agrs):
  if new_pw.get() == "":
    state_label.configure(text="")
  elif new_pw.get() == confirm_pw.get():
    state_label.configure(text="패스워드 일치!", foreground="green")
  else:
    state_label.configure(text="에러: 패스워드 불일치!", foreground="red")

def change_btn_func():
  if new_pw.get() == "":
    state_label.configure(text="")
  elif new_pw.get() == confirm_pw.get():
    state_label.configure(text="패스워드 변경 완료!", foreground="green")
  else:
    state_label.configure(text="에러: 패스워드 변경 취소!", foreground="red")

# 윈도우 생성
window = Tk()
window.geometry("500x130")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# 데이터
new_pw = StringVar()
confirm_pw = StringVar()
confirm_pw.trace("w", validate)

# UI 만들고 배치
state_label = Label(window, text="")
state_label.grid(column=0, row=0, columnspan=3, padx=5, pady=5)
Label(window, text="New Password:").grid(column=0, row=1, padx=5, pady=5)
Label(window, text="Confirm Password:").grid(column=0, row=2, padx=5, pady=5)

new_entry = Entry(window, textvariable=new_pw, show="*")
new_entry.grid(column=1, row=1, padx=5, pady=5)
new_entry.focus()

confirm_entry = Entry(window, textvariable=confirm_pw, show="*")
confirm_entry.grid(column=1, row=2, padx=5, pady=5)

change_btn = Button(window, text="Change", command=change_btn_func)
change_btn.grid(column=1, row=3, padx=5, pady=5)

# 윈도우 실행
window.mainloop()