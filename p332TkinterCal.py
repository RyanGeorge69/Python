from tkinter import *

def add():
    x=int(txtno1.get())
    y=int(txtno.get())
    stradd.set(str(x+y))
def sub():
    x=int(txtno1.get())
    y=int(txtno.get())
    stradd.set(str(x-y))
def mul():
    x=int(txtno1.get())
    y=int(txtno.get())
    stradd.set(str(x*y))
def div():
    x=int(txtno1.get())
    y=int(txtno.get())
    stradd.set(str(x/y))

root=Tk()
root.geometry("250x150")

stradd = StringVar(root)

lblno = Label(root,text = "No1")
lblno.grid(row = 1, column = 0)
txtno1 = Entry(root)
txtno1.grid(row = 1, column = 1)
lblno = Label(root,text = "No2")
lblno.grid(row = 2, column = 0)
txtno = Entry(root)
txtno.grid(row = 2, column = 1)


btnSubmit = Button(root, text = "-",command=sub )
btnSubmit.grid(row = 3, column = 1)
btnSubmit = Button(root, text = "X",command=mul )
btnSubmit.grid(row = 3, column = 2)
btnSubmit = Button(root, text = "/",command=div )
btnSubmit.grid(row = 3, column = 3)
btnSubmit = Button(root, text = "+" ,command=add)
btnSubmit.grid(row = 3, column = 4)

btnSubmit.grid(row = 3, column = 0)

lbladd =Label(root,text = "Answer")
lbladd.grid(row = 4, column = 0)
txtadd =Entry(root,textvariable=stradd)
txtadd.grid(row = 4, column = 1)
root.mainloop()
