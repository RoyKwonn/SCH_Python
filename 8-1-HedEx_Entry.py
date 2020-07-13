from tkinter import *

def save_data():
    fileD = open("deliveries.txt", "a")
    fileD.write("창고 : ")
    fileD.write("%s\n" % depot.get())
    fileD.write("배달품목 : ")
    fileD.write("%s\n" % description.get())
    fileD.write("주소 : ")
    fileD.write("%s\n" % address.get("1.0", END))
    depot.delete(0, END)
    description.delete(0, END)
    address.delete("1.0", END)

app = Tk()
app.title('Head-Ex Deliveries')

Label(app, text="창고 : ").pack()
depot = Entry(app)
depot.pack()

Label(app, text="배달품목 : ").pack()
description = Entry(app)
description.pack()

Label(app, text ="주소 : ").pack()
address = Text(app)
address.pack()

Button(app, text ="저장", command = save_data).pack()

app.mainloop()
