from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI")
        self.geometry("500x500")
        self.label=Label(self,text="Hello World",font=("Arial",20))
        self.label.pack()
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvariable=self.var,relief=SUNKEN,anchor=W)
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("Clicked")

    def createbutton(self,inptext):
        Button(self,text=inptext,command=self.click).pack()
if __name__=="__main__":
    gui=GUI()
    gui.status()
    gui.createbutton("Click Me")
    gui.mainloop()