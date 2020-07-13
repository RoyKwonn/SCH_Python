from tkinter import *
import pygame.mixer # as mixer 이렇게 사용해도 된다 

app = Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')

sound_file = "mix_sound/50459_M_RED_Nephlimizer.wav" # 연주할 음악 파일

mixer = pygame.mixer
mixer.init()    # 사운드 시스템 시작

def track_start():
    track.play(loops=-1) # play() 함수에 loops 인자 값을 -1로 지정하면 stop()을 호출할 때까지 계속 반복 연주

def track_stop():
    track.stop()

def shutdown():
    track.stop()
    app.destroy()

track=mixer.Sound(sound_file) # 사운드 파일 로드

start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

stop_button = Button(app, command = track_stop, text = "Stop")
stop_button.pack(side = RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown) # window 종료시 호출되는 함수 등록

app.mainloop()
