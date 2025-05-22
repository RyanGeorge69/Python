from tkinter import *
ryan_root=Tk()
ryan_root.geometry("500x500")
# to give icon to the window
# ryan_root.wm_iconbitmap("1.ico")

width=ryan_root.winfo_screenwidth()
height=ryan_root.winfo_screenheight()
print(f"{width}X{height}")

Button(text="Click Me",fg="red",bg="blue",command=ryan_root.destroy).pack()

ryan_root.mainloop()