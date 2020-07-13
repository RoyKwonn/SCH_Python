from tkinter import *

def save_data():
    fileD = open("deliveries.txt", "a")
    fileD.write("창고 : ")
    fileD.write("%s\n" % depot.get())
    fileD.write("배달품목 : ")
    fileD.write("%s\n" % description.get())
    fileD.write("주소 : ")
    fileD.write("%s\n" % address.get("1.0", END))
    depot.set(None)
    description.delete(0, END)
    address.delete("1.0", END)

def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

app = Tk()
app.title('Head-Ex Deliveries')

Label(app, text="창고 : ").grid(row=0, column=0)
depot = StringVar()
depot.set(None)
options = read_depots("depots.txt")
OptionMenu(app, depot, *options).grid(row=0, column=1)

Label(app, text="배달품목 : ").grid(row=0, column=2)
description = Entry(app)
description.grid(row=0, column=3)

Label(app, text ="주소 : ").grid(row=1, column=0)
address = Text(app, width=30, height=5)
address.grid(row=1, column=1)

Button(app, text ="저장", command = save_data).grid(row=1, column=3)

app.mainloop()
