from tkinter import *

counter = 0

def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count) # after() method를 사용하여 1000ms 후에 count() 함수 호출(스레드)
    count()

app = Tk()
app.title("Counting Seconds")
label = Label(app, fg="green")
label.pack()
counter_label(label)

b1 = Button(app, text = 'Stop', width = 25, command = app.destroy)
b1.pack()

app.mainloop() # window의 event를 기다리고 있다 


