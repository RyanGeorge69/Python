from tkinter import *

window=Tk()
var = IntVar()
entryText = IntVar(window)
stradd = StringVar(window)
window.geometry("250x150")

def cal():
    entryText.set(int(var.get()))
    x = int(txtno1.get())
    y = int(txtno2.get())
    if entryText.get()==1:
        stradd.set(str(x+y))
    elif entryText.get()==2:
        stradd.set(str(x-y))
    elif entryText.get() == 3:
        stradd.set(str(x * y))
    elif entryText.get()==4:
        stradd.set(str(x/y))

lblno1 = Label(window,text = "number=")
lblno1.grid(row = 1, column = 0)
txtno1 = Entry(window)
txtno1.grid(row = 1, column = 1,columnspan=4)
lblno1 = Label(window,text = "number=")
lblno1.grid(row = 2, column = 0)
txtno2 = Entry(window)
txtno2.grid(row = 2, column = 1,columnspan=4)

rdbbtn1 = Radiobutton(window, text="+",variable=var, value=1)
rdbbtn1.grid(row=0,column=1)
rdbbtn2 = Radiobutton(window, text="-",variable=var, value=2)
rdbbtn2.grid(row=0,column=2)
rdbbtn1 = Radiobutton(window, text="X",variable=var, value=3)
rdbbtn1.grid(row=0,column=3)
rdbbtn2 = Radiobutton(window, text="/",variable=var, value=4)
rdbbtn2.grid(row=0,column=4)
# command=Greater
btnSubmit = Button(window, text = "Summit",command=cal)
btnSubmit.grid(row = 3, column = 0)

lblno1 = Label(window,text = "Answer=")
lblno1.grid(row = 4, column = 0)
txtno3 = Entry(window,textvariable = stradd)
txtno3.grid(row = 4, column = 1,columnspan=4)

window.mainloop()