from tkinter import *
import pygame.mixer # as mixer 이렇게 사용해도 된다 

app = Tk()
app.title("Head First Mix")
app.geometry('400x100+200+100')

sound_file = "mix_sound/50459_M_RED_Nephlimizer.wav" # 연주할 음악 파일

mixer = pygame.mixer
mixer.init()    # 사운드 시스템 시작



def track_toggle():
    if track_playing.get() == 1:
        track.play(loops=-1)
    else:
        track.stop()

def change_volume(v):
    # Scale 클ㄹ래스 내에서 호출 시 인수 포함
    # 스케일 값을 나타내는 인수
    track.set_volume(volume.get()) # track.set_volume(float(v))



def shutdown():
    track.stop()
    app.destroy() # 오류 안나게 넣어주어야함.

track=mixer.Sound(sound_file) # 사운드 파일 로드

track_playing = IntVar()
track_button = Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file)
track_button.pack(side=LEFT)

volume = DoubleVar()
volume.set(track.get_volume())
volume_scale = Scale(variable = volume, from_ = 0.0, to = 1.0, resolution = 0.1, command = change_volume, label="Volume", orient = HORIZONTAL)
volume_scale.pack(side=RIGHT)
                           
app.protocol("WM_DELETE_WINDOW", shutdown) # window 종료시 호출되는 함수 등록

app.mainloop()
