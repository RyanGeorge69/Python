from tkinter import *
ryan_root=Tk()
ryan_root.geometry("500x500")

def harry(event):
    print(f"You clicked ont the button at {event.x} , {event.y}")

widge=Button(ryan_root,text="Click Me",fg="red",bg="blue")
widge.pack()
widge.bind("<Button-1>",harry)
widge.bind("<Double-1>",quit)

ryan_root.mainloop()