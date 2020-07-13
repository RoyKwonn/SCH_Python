from tkinter import *

app = Tk()
app.title('위젯 테두리')

Label(app, borderwidth = 1, width = 40, relief="raised", text="raised & borderwidth=1").pack()
Label(app, borderwidth = 2, width = 40, relief="ridge", text="ridge & borderwidth=2").pack()
Label(app, borderwidth = 3, width = 40, relief="sunken", text="sunken & borderwidth=3").pack()
Label(app, borderwidth = 4, width = 40, relief="flat", text="flat & borderwidth=4").pack()
Label(app, borderwidth = 5, width = 40, relief="groove", text="groove & borderwidth=5").pack()
Label(app, borderwidth = 6, width = 40, relief="solid", text="solid & borderwidth=6").pack()

app.mainloop()
