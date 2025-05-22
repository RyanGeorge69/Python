from tkinter import *

window = Tk()
window.geometry("500x100+400+400")
window.title('Spin Color Demo')

def _from_rgb(rgb):
     return "#%02x%02x%02x" % rgb

def clicked():
    r = int(spinRed.get())
    g = int(spinGreen.get())
    b = int(spinBlue.get())
    window.configure(bg=_from_rgb((r, g, b)))
lblColor = Label(window,text = "Color").grid(row = 0, column = 0)

spinRed = Spinbox(window, from_=0, to=255)
spinRed.grid(row = 0, column = 1)
spinGreen = Spinbox(window, from_=0, to=255)
spinGreen.grid(row = 0, column = 2)
spinBlue = Spinbox(window, from_=0, to=255)
spinBlue.grid(row = 0, column = 3)

btnSubmit = Button(window, text = "Submit",command=clicked).grid(row = 1, column = 0)

window.mainloop()