# # 윈도우 만들기
# from tkinter import *

# # 화면 생성
# window = Tk()
# window.title("window name")
# window.geometry("500x500")
# window.resizable(width=FALSE, height=TRUE)

# # 메인루프 실행
# window.mainloop()


# 라벨 만들기
from tkinter import *

# 화면 생성
window = Tk()
window.title("window name")
window.geometry("500x500")
window.resizable(width=FALSE, height=TRUE)

# UI 생성
label = Label(window, text="라벨입니다.")

# UI 배치
label.pack()

# 메인루프 실행
window.mainloop()