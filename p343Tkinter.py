from tkinter import *
def clicked():
    print(checkvar1.get(), checkvar2.get(),checkvar3.get(),checkvar4.get())
def clicked():
    c=checkvar1.get()
    SQL=checkvar2.get()
    Java=checkvar3.get()
    Python=checkvar4.get()
    str=""
    if c==1:
        str=str + " C "
    if SQL==1:
        str = str + " C++ "
    if Java==1:
        str = str + " Java "
    if Python==1:
        str = str + " Python "
    StringAns.set(str)

window = Tk()
window.title('CheckBox Demo')
window.geometry("500x150")
lblNo = Label(window,text = "No").grid(row = 0, column = 0)
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()
entryText = StringVar(window)
StringAns = StringVar(window)


chkbtn1 = Checkbutton(window, text="C", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10)
chkbtn1.grid(row=0,column=1)

chkbtn2 = Checkbutton(window, text="C++", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)
chkbtn2.grid(row=0,column=2)

chkbtn3 = Checkbutton(window, text="Java", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)
chkbtn3.grid(row=0,column=3)

chkbtn4 = Checkbutton(window, text="Python", variable=checkvar4, onvalue=1, offvalue=0, height=2, width=10)
chkbtn4.grid(row=0,column=4)

btnSubmit = Button(window, text = "Submit",command=clicked).grid(row = 2, column = 0)

lblAns = Label(window,text = "Ans").grid(row = 3, column = 0)
txtAns = Entry(window,textvariable = StringAns).grid(row = 3, column = 1)

window.mainloop()

