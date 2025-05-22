from tkinter import *
from PIL import ImageTk,Image
ryan_root=Tk()
# to give the size of the box in the output
# can increase the size of the box
ryan_root.geometry("500x500")

# cannot make it smaller than the range
ryan_root.minsize(300,300)

# cannot make it larger than the range
ryan_root.maxsize(600,600)

# to add text in the gui (text for what you want to write and font
text=Label(text="hi",font=("Arial",20))
text.pack()

# to give the title of the box
"""
Important label options:
text, 
font
way 1=font=("Arial",20,"bold")
way 2=font="Arial 20 bold"
fg(foreground)
bg(background),
bd(border width), 
relief(border style)=SUNKEN, RAISED, GROOVE, RIDGE
padx(x padding)
pady(y padding)
"""
ryan_root.title("Ryan's GUI")
title=Label(text="Ryan's GUI",bg="red",fg="white",font=("Arial",20,"bold"),padx=10,pady=50,borderwidth=1,relief=GROOVE)

"""
Important pack options:
anchor=nw(northwest),ne(northeast),sw(southwest),se(southeast),center
side=top,bottom,left,right
fill=x,y,both,none
expand=True,False
"""
title.pack(anchor="se",side="bottom",fill=X)
title.pack(side=LEFT,fill=Y)

ryan_root.mainloop()