from tkinter import *

def clicked():
    value = listbox.get(listbox.curselection())
    entryText.set(value)
window = Tk()
window.title('List Demo')
window.geometry("400x250")

var = IntVar()
entryText = StringVar(window)


lblAnimal = Label(window,text = "Animal").grid(row = 0, column = 0)

listbox = Listbox(window)

listbox.insert(1, "lion")
listbox.insert(2, "tiger")
listbox.insert(3, "zebra")
listbox.insert(4, "elephant")
listbox.insert(5, "deer")
listbox.insert(6, "fox")
listbox.insert(7, "Wolf")
listbox.insert(8, "Gorilla")
listbox.insert(9, "Jackal")
listbox.insert(10, "Otter")

listbox.grid(row = 0, column = 1)

btnSubmit = Button(window, text = "Submit",command=clicked).grid(row = 2, column = 0)

lblAns = Label(window,text = "Ans").grid(row = 3, column = 0)

txtAns = Entry(window,textvariable = entryText).grid(row = 3, column = 1)

window.mainloop()
