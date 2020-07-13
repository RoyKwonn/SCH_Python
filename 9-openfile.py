from tkinter import *
import tkinter.messagebox as mb
from tkinter import filedialog as fd # = import tkinter.filedialog as fd

def call_back():
    name = fd.askopenfilename()
    # name = fd.asksaveasfilename()
    mb.showinfo("오픈파일 이름", name)

app = Tk()
app.title("오픈파일 테스트")
app.geometry('300x50+200+200')

Button(app, text='파일오픈', command=call_back).pack(side='bottom')


app.mainloop()
