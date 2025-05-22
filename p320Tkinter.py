from tkinter import *
ryan_root=Tk()
ryan_root.geometry("500x500")

frame=Frame(ryan_root,borderwidth=10)
frame.pack(side=LEFT,fill=Y)
def hi():
    print("hi")

b1=Button(frame,text="HI",fg="red",bg="blue",command=hi)
b1.pack()
b2=Button(frame,text="HI",fg="red",bg="blue")
b2.pack(side=TOP)
ryan_root.mainloop()