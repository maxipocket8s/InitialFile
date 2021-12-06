from tkinter import *
import time
import datetime

def time_tick():
    real_time = datetime.datetime.now()
    delay_time = real_time - datetime.timedelta(minutes=15)
    c_time = delay_time.strftime("%H:%M:%S")
    c_frame.config(text=c_time, font=("맑은고딕", 60, "bold"), fg="#000000")
    c_frame.after(200, time_tick)

c_window =Tk()
c_window.title("15분 대기 시계")
c_window.config(background="#ffffff")
c_window.resizable(True, True)
c_blank_top = Frame(c_window, width=400, height=10, bg="#ffffff")
c_blank_top.pack()
c_frame = LabelFrame(c_window, width=320, height=100, bd=0, bg="#ffffff")
c_frame.pack()
c_blank_bottom = Frame(c_window, width=400, height=10, bg="#ffffff")
c_blank_bottom.pack()

time_tick()
c_window.mainloop()