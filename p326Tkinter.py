from time import sleep
from tkinter import *
from tkinter import messagebox as tmsg
ryan_root=Tk()
ryan_root.geometry("500x500")

def hi():
    print("hi")
def hello():
    print("hello")
    tmsg.showinfo("Hello","Hello World")

# mymenu=Menu(ryan_root)
# mymenu.add_command(label="New", command=hi)
# ryan_root.config(menu=mymenu)

yours=Menu(ryan_root)

m1=Menu(yours,tearoff=0)
m1.add_command(label="New", command=hi)
yours.add_cascade(label="File", menu=m1)
# m1.add_radiobutton(label="One")
# m1.add_separator()
# m1.add_radiobutton(label="Two")
m1.add_command(label="Hello", command=hello)

ryan_root.config(menu=yours)


ryan_root.mainloop()