from tkinter import *

def areaTri():
    x=int(txtno1.get())
    y=int(txtno.get())
    stradd.set(str(.5*x*y))






root=Tk()
root.geometry("250x150")

stradd = StringVar(root)

lblno = Label(root,text = "Base")
lblno.grid(row = 1, column = 0)
txtno1 = Entry(root)
txtno1.grid(row = 1, column = 1)
lblno = Label(root,text = "Height")
lblno.grid(row = 2, column = 0)
txtno = Entry(root)
txtno.grid(row = 2, column = 1)

btnSubmit = Button(root, text = "Area of triangle",command=areaTri )
btnSubmit.grid(row = 3, column = 1)



btnSubmit.grid(row = 3, column = 0)

lbladd =Label(root,text = "Answer")
lbladd.grid(row = 4, column = 0)
txtadd =Entry(root,textvariable=stradd)
txtadd.grid(row = 4, column = 1)
root.mainloop()
