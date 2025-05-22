from tkinter import *

def Greater():
    x=int(txtno.get())
    y=int(txtno1.get())
    if x>y:
        stradd.set(str(f"{x} is grater"))
    elif x<y:
        stradd.set(str(f"{y} is grater"))
    else:
        stradd.set(str("Both are same"))

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



btnSubmit = Button(root, text = "Greater no,",command=Greater )
btnSubmit.grid(row = 3, column = 0)

lbladd =Label(root,text = "Answer")
lbladd.grid(row = 4, column = 0)
txtadd =Entry(root,textvariable=stradd)
txtadd.grid(row = 4, column = 1)
root.mainloop()
