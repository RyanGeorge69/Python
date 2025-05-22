from tkinter import *

window = Tk()
window.geometry("300x100+400+400")
window.title('Spin Demo')

def clicked():
    value=spin.get()
    entryText.set(str(value))
entryText = StringVar(window)

lblNo = Label(window,text = "No").grid(row = 0, column = 0)

spin = Spinbox(window, from_=1, to=1000000000000)
spin.grid(row = 0, column = 1)

btnSubmit = Button(window, text = "Submit",command=clicked).grid(row = 1, column = 0)

lblAns = Label(window,text = "Ans").grid(row = 2, column = 0)
txtAns = Entry(window,textvariable = entryText).grid(row = 2, column = 1)

window.mainloop()
