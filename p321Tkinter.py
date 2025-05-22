from tkinter import *
ryan_root=Tk()
ryan_root.geometry("500x500")

def getvals():
    # to get the value from the user
    print(user_input.get())
    print(password_input.get())


user=Label(ryan_root,text="Username")
password=Label(ryan_root,text="Password")
user.grid(row=0,column=0)
password.grid(row=1,column=0)

"""
Variable classes in tkinter:
IntVar, DoubleVar, StringVar, BooleanVar
"""
user_input=StringVar()
password_input=StringVar()


user_entry=Entry(ryan_root,textvariable=user_input)
password_entry=Entry(ryan_root,textvariable=password_input)
user_entry.grid(row=0,column=1)
password_entry.grid(row=1,column=1)

Button(ryan_root,text="Login",command=getvals).grid(row=3,column=1)


ryan_root.mainloop()