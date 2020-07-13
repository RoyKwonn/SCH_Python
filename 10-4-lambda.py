from tkinter import *
import tkinter.messagebox as mb

def bttype(s):
    global mt
    mt = s

def btclick(m, s):
    if m == "에러":
        mb.showerror(m, s)
    elif m == "경고":
        mb.showwarning(m, s)
    else:
        mb.showinfo(m, s)

def shutdown():
    app.destroy()


app = Tk()
app.title("Lambda")
app.geometry('200x100+200+200')

b1 = Button(app, text='에러', command = lambda: bttype("에러"))
b2 = Button(app, text='경고', command = lambda: bttype("경고"))
b3 = Button(app, text='눌러주세요', command = lambda: btclick(mt, mt+" 메시지"))

b1.grid(row=0, column=0, padx=5, pady=5)
b2.grid(row=0, column=1, padx=5, pady=5)
b3.grid(row=1, columnspan=2, padx=5, pady=5)

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
