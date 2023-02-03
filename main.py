from tkinter import *

win = Tk() # 창 생성

win.title("탄력적 습관") # 창 제목
win.geometry("1366x768") # 창 크기 가로x세로
win.option_add("*Font", "맑은고딕 25")

btn = Button(win, text="버튼")
btn.pack()

win.mainloop() # 창 실행




# # 습관
# def habits():
#     pass
#
# input("사용하실 습관 3가지를 입력해주세요 :")