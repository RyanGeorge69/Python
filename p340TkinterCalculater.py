from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("300x210")
str1 = StringVar(root)
strno=StringVar(root)
op=StringVar(root)

def div():
    strno.set(str1.get())
    str1.set("")
    op.set("/")

def mul():
    strno.set(str1.get())
    str1.set("")
    op.set("*")

def sub():
    strno.set(str1.get())
    str1.set("")
    op.set("-")

def add():
    strno.set(str1.get())
    str1.set("")
    op.set("+")

def equal():
    if op.get()=="/":
        str1.set(str(float(strno.get())/float(str1.get())))
    elif op.get()=="*":
        str1.set(str(float(strno.get())*float(str1.get())))
    elif op.get()=="-":
        str1.set(str(float(strno.get())-float(str1.get())))
    elif op.get()=="+":
        str1.set(str(float(strno.get())+float(str1.get())))
    else:
        str1.set("Error")

def ac():
    str1.set("")
    op.set("")
    strno.set("")
def squre():
    str1.set(str(float(str1.get())*float(str1.get())))
def cube():
    str1.set(str(float(str1.get())*float(str1.get())*float(str1.get())))


def funone():
    str1.set(str1.get()+str(1))
def funtwo():
    str1.set(str1.get()+str(2))
def funthree():
    str1.set(str1.get()+str(3))
def funfour():
    str1.set(str1.get()+str(4))
def funfive():
    str1.set(str1.get() + str(5))
def funsix():
    str1.set(str1.get()+str(6))
def funseven():
    str1.set(str1.get()+str(7))
def funeight():
    str1.set(str1.get()+str(8))
def funnine():
    str1.set(str1.get()+str(9))
def funzero():
    str1.set(str1.get()+str(0))
def funpoint():
    str1.set(str1.get()+str("."))
def addsub():
    str1.set(str(-int(str1.get())))

txtno1 = Entry(root,textvariable=str1)
txtno1.grid(row = 1, column = 0,columnspan=4)
btn =Button(root, text="Ac",command=ac)
btn.grid(row=2, column=0, padx=5, pady=5)
btn =Button(root, text="x²",command=squre)
btn.grid(row=2, column=1, padx=5, pady=5)
btn =Button(root, text="x³",command=cube)
btn.grid(row=2, column=2, padx=5, pady=5)
btn =Button(root, text="÷",command=div)
btn.grid(row=2, column=3, padx=5, pady=5)
btn =Button(root, text="X",command=mul)
btn.grid(row=3, column=3, padx=5, pady=5)
btn =Button(root, text="-",command=sub)
btn.grid(row=4, column=3, padx=5, pady=5)
btn =Button(root, text="+",command=add)
btn.grid(row=5, column=3, padx=5, pady=5)
btn =Button(root, text="=",command=equal)
btn.grid(row=6, column=3, padx=5, pady=5)
btn =Button(root, text="+/-",command=addsub)
btn.grid(row=6, column=0, padx=5, pady=5)

btn =Button(root, text="7",command=funseven)
btn.grid(row=3, column=0, padx=5, pady=5)
btn =Button(root, text="4",command=funfour)
btn.grid(row=4, column=0, padx=5, pady=5)
btn =Button(root, text="1",command=funone)
btn.grid(row=5, column=0, padx=5, pady=5)
btn =Button(root, text="8",command=funeight)
btn.grid(row=3, column=1, padx=5, pady=5)
btn =Button(root, text="5",command=funfive)
btn.grid(row=4, column=1, padx=5, pady=5)
btn =Button(root, text="2",command=funtwo)
btn.grid(row=5, column=1, padx=5, pady=5)
btn =Button(root, text="9",command=funnine)
btn.grid(row=3, column=2, padx=5, pady=5)
btn =Button(root, text="6",command=funsix)
btn.grid(row=4, column=2, padx=5, pady=5)
btn =Button(root, text="3",command=funthree)
btn.grid(row=5, column=2, padx=5, pady=5)
btn =Button(root, text="0",command=funzero)
btn.grid(row=6, column=1, padx=5, pady=5)
btn =Button(root, text=".",command=funpoint)
btn.grid(row=6, column=2, padx=5, pady=5)


root.mainloop()