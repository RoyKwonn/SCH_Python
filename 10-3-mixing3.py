from tkinter import *
from sound_panel1 import *
import pygame.mixer
import os

app = Tk()
app.title("Head First Mix")
mixer = pygame.mixer
mixer.init()

def shutdown():
    mixer.stop()
    app.destroy()

dirList = os.listdir("mix_sound")
for fname in dirList:
    if fname.endswith(".wav"):
        panel = SoundPanel(app, mixer, "mix_sound/" + fname)
        panel.pack()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
