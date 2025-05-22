from tkinter import *
window = Tk()
window.title('School Form')
window.geometry("250x150")


lblName = Label(window,text = "Name").grid(row = 0, column = 0)
lblSchool = Label(window,text = "School", fg="red").grid(row = 1, column = 1)

lblStd = Label(window,text = "Std").grid(row = 2, column = 0)
lblDiv = Label(window,text = "Div",font=("Helvetica", 18)).grid(row = 3, column = 0)

txtName=Entry(window, text="This is Label widget",fg='red', bg='black',font=("Helvetica", 16))
window.mainloop()
