from tkinter import *

window=Tk()
stradd = StringVar(window)
window.geometry("300x300")

def add():
    x=int(txtno1.get())
    y=int(txtno2.get())
    stradd.set(str(x+y))
def sub():
    x = int(txtno1.get())
    y = int(txtno2.get())
    stradd.set(str(x - y))
def mul():
    x = int(txtno1.get())
    y = int(txtno2.get())
    stradd.set(str(x * y))
def div():
    x = int(txtno1.get())
    y = int(txtno2.get())
    stradd.set(str(x / y))

window.title('Message Demo')
window.geometry("350x250")

menubar = Menu(window)
m1=Menu(menubar,tearoff=0)
menubar.add_cascade(label="op",menu=m1)
m1.add_command(label="+", command=add)
m1.add_command(label="-", command=sub)
m1.add_command(label="X", command=mul)
m1.add_command(label="/", command=div)
window.config(menu=menubar)

lblno1 = Label(window,text = "number=")
lblno1.grid(row = 1, column = 0)
txtno1 = Entry(window)
txtno1.grid(row = 1, column = 1,columnspan=4)
lblno1 = Label(window,text = "number=")
lblno1.grid(row = 2, column = 0)
txtno2 = Entry(window)
txtno2.grid(row = 2, column = 1,columnspan=4)

lblno1 = Label(window,text = "Answer=")
lblno1.grid(row = 4, column = 0)
txtno3 = Entry(window,textvariable = stradd)
txtno3.grid(row = 4, column = 1,columnspan=4)
window.mainloop()