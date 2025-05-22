from tkinter import *

def Greater():
    x=int(txtno.get())
    y=int(txtno1.get())
    z=int(txtno2.get())
    if x>y and x>z:
        stradd.set(str(f"{x} is grater"))
    elif x<y and z<y:
        stradd.set(str(f"{y} is grater"))
    elif x<z and y<z:
        stradd.set(str(f"{z} is grater"))
    else:
        stradd.set(str("Some no are same"))

root=Tk()
root.geometry("250x150")

stradd = StringVar(root)

lblno = Label(root,text = "No 1=")
lblno.grid(row = 1, column = 0)
txtno = Entry(root)
txtno.grid(row = 1, column = 1)
lblno1 = Label(root,text = "No 2=")
lblno1.grid(row = 2, column = 0)
txtno1 = Entry(root)
txtno1.grid(row = 2, column = 1)
lblno2 = Label(root,text = "No 3=")
lblno2.grid(row = 3, column = 0)
txtno2 = Entry(root)
txtno2.grid(row = 3, column = 1)



btnSubmit = Button(root, text = "Greater no,",command=Greater )
btnSubmit.grid(row = 4, column = 0)

lbladd =Label(root,text = "Answer")
lbladd.grid(row = 5, column = 0)
txtadd =Entry(root,textvariable=stradd)
txtadd.grid(row = 5, column = 1)
root.mainloop()
