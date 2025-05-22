from tkinter import *
window=Tk()
window.geometry("200x300")

txtName=Entry(window, fg='red',bg='black', font=("Helvetica", 16))
txtName.place(x=60, y=5)

txtfld=Entry(window, bd=10)
txtfld.place(x=50, y=50)

txtPwd=Entry(window, show="a")
txtPwd.place(x=100, y=100)

window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()
