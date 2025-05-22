from tkinter import *

def Greater():
    x=int(txtno.get())
    z=[]
    for i in range(1,x+1):
        z.append(i)
    stradd.set(str(z))
        

root=Tk()
root.geometry("250x150")

stradd = StringVar(root)

lblno = Label(root,text = "No 1=")
lblno.grid(row = 1, column = 0)
txtno = Entry(root)
txtno.grid(row = 1, column = 1)




btnSubmit = Button(root, text = "Greater no,",command=Greater )
btnSubmit.grid(row = 4, column = 0)

lbladd =Label(root,text = "Answer")
lbladd.grid(row = 5, column = 0)
txtadd =Entry(root,textvariable=stradd)
txtadd.grid(row = 5, column = 1)
root.mainloop()
