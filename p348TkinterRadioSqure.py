from tkinter import *

window=Tk()
var = IntVar()
entryText = IntVar(window)
stradd = IntVar(window)
window.geometry("250x150")

def pow1():
    entryText.set(int(var.get()))
    x = int(txtno1.get())
    if entryText.get()==1:
        stradd.set(x * x)
    elif entryText.get()==2:
        stradd.set(x * x * x)

lblno1 = Label(window,text = "number=")
lblno1.grid(row = 1, column = 0)
txtno1 = Entry(window)
txtno1.grid(row = 1, column = 1,columnspan=4)

rdbbtn1 = Radiobutton(window, text="x²",variable=var, value=1)
rdbbtn1.grid(row=0,column=1)
rdbbtn2 = Radiobutton(window, text="x³",variable=var, value=2)
rdbbtn2.grid(row=0,column=2)
# command=Greater
btnSubmit = Button(window, text = "Summit",command=pow1)
btnSubmit.grid(row = 2, column = 0)

lblno1 = Label(window,text = "Answer=")
lblno1.grid(row = 3, column = 0)
txtno2 = Entry(window,textvariable = stradd)
txtno2.grid(row = 3, column = 1,columnspan=4)

window.mainloop()