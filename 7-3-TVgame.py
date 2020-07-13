from tkinter import *
import pygame.mixer


sounds = pygame.mixer
sounds.init()
correct_s = sounds.Sound("sound/correct.wav")
wrong_s = sounds.Sound("sound/wrong.wav")

number_correct = 0
number_wrong = 0

def play_correct_sound():
    global number_correct
    number_correct = number_correct + 1
    correct_s.play()

def play_wrong_sound():
    global number_wrong
    number_wrong = number_wrong + 1
    wrong_s.play()

app = Tk()
app.title("TVN 게임 쇼")
app.geometry('300x110+200+100')

b1 = Button(app, text = "정답", width = 10, command = play_correct_sound)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "오답", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)


app.mainloop() # window의 event를 기다리고 있다 

print("정답 수 : " + str(number_correct))
print("오답 수 : " + str(number_wrong))


