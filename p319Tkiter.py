from tkinter import *
ryan_root=Tk()
ryan_root.geometry("500x500")
f1=Frame(ryan_root,bg="blue",borderwidth=10,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

f2=Frame(ryan_root,bg="red",borderwidth=10,relief=SUNKEN)
f2.pack(side=TOP,fill=X)

l=Label(f1,text="Ryan's GUI",bg="blue",fg="white")
l.pack()
l=Label(f2,text="Ryan's GUI",bg="red",fg="white")
l.pack()
ryan_root.mainloop()