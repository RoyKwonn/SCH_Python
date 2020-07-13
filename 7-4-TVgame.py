from tkinter import *
import pygame.mixer

def play_correct_sound():
    num_good.set(num_good.get() + 1)
    correct_s.play()
    num_tot.set(num_good.get() + num_bad.get())

def play_wrong_sound():
    num_bad.set(num_bad.get() + 1)
    wrong_s.play()
    num_tot.set(num_good.get() + num_bad.get())

app = Tk()
app.title("TVN 게임 쇼")
app.geometry('300x110+200+100')

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("sound/correct.wav")
wrong_s = sounds.Sound("sound/wrong.wav")

num_good = IntVar()
num_good.set(0)
num_bad = IntVar()
num_bad.set(0)

num_tot = IntVar()
num_tot.set(0)

lab = Label(app, text='버튼을 누르세요', height = 3)
lab.pack()

lab1 = Label(app, textvariable = num_good)
lab1.pack(side = 'left')

lab2 = Label(app, textvariable = num_bad)
lab2.pack(side = 'right')

Label(app, textvariable=num_tot).pack(side='bottom')

b1 = Button(app, text = "정답", width = 10, command = play_correct_sound)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "오답", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)


app.mainloop() # window의 event를 기다리고 있다 


