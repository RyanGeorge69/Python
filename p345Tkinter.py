from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Message Demo')
window.geometry("350x250+400+400")

def hello():
    messagebox.showinfo("showinfo", "Information")

def helloQuit():
    window.quit()
menubar = Menu(window)

menubar.add_command(label="Hello!", command=hello)

menubar.add_command(label="Quit!", command=helloQuit)

window.config(menu=menubar)

window.mainloop()

