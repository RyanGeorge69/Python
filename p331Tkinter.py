from tkinter import *

def square():
    x=int(txtno.get())
    strSqaure.set(str(x*x))

ryan_root=Tk()
ryan_root.geometry("250x150")
strSqaure = StringVar(ryan_root)

lblno = Label(ryan_root,text = "No")
lblno.grid(row = 1, column = 0)
txtno = Entry(ryan_root)
txtno.grid(row = 1, column = 1)

btnSubmit = Button(ryan_root, text = "Submit" ,command=square)
btnSubmit.grid(row = 2, column = 0)

lbladd =Label(ryan_root,text = "Add")
lbladd.grid(row = 3, column = 0)
txtadd =Entry(ryan_root,textvariable=strSqaure)
txtadd.grid(row = 3, column = 1)
ryan_root.mainloop()
