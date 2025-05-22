from tkinter import *

def areacir():
    x=int(txtno1.get())
    stradd.set(str(3.14*x*x))

root=Tk()
root.geometry("250x150")

stradd = StringVar(root)

lblno = Label(root,text = "Radius")
lblno.grid(row = 1, column = 0)
txtno1 = Entry(root)
txtno1.grid(row = 1, column = 1)


btnSubmit = Button(root, text = "Area of Circle",command=areacir )
btnSubmit.grid(row = 3, column = 1)



btnSubmit.grid(row = 3, column = 0)

lbladd =Label(root,text = "Answer")
lbladd.grid(row = 4, column = 0)
txtadd =Entry(root,textvariable=stradd)
txtadd.grid(row = 4, column = 1)
root.mainloop()
