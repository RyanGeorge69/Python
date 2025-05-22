from tkinter import *

def clicked():
    num = int(entry_number.get())
    for i in range(1, 11):
        text_output.insert(END, f"{i}X{num}={i*num}\n")

root=Tk()
root.title("Multiline Text Display")
root.geometry("300x300")

lblno=Label(root, text="No")
lblno.grid(row=0, column=0, padx=5, pady=5)
entry_number = Entry(root)
entry_number.grid(row=0, column=1, padx=5, pady=5)

btnSubmit=Button(root, text="Submit", command=clicked)
btnSubmit.grid(row=1, column=0, padx=5, pady=5)

lblprint=Label(root, text="Ans")
lblprint.grid(row=2, column=0, padx=5, pady=5)
text_output = Text(root, width=20, height=10)
text_output.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()