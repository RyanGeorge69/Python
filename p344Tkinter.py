from tkinter import *

def clicked():
    entryText.set(str(var.get()))

window = Tk()
window.title('Radio Demo')
window.geometry("500x150")
var = IntVar()
entryText = StringVar(window)

lblNo = Label(window,text = "No").grid(row = 0, column = 0)

rdbbtn1 = Radiobutton(window, text="C",variable=var, value=1)
rdbbtn1.grid(row=0,column=1)

rdbbtn2 = Radiobutton(window, text="C++",variable=var, value=2)
rdbbtn2.grid(row=0,column=2)

rdbbtn3 = Radiobutton(window, text="Java",variable=var, value=3)
rdbbtn3.grid(row=0,column=3)

btnSubmit = Button(window, text = "Submit",command=clicked).grid(row = 2, column = 0)
lblAns = Label(window,text = "Ans").grid(row = 3, column = 0)
txtAns = Entry(window,textvariable = entryText).grid(row = 3, column = 1)

window.mainloop()
