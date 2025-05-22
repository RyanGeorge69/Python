from tkinter import *
from tkinter import messagebox

t=1
root = Tk()
root.title("Tic Tac Toe")
str1 = StringVar(root)
str2 = StringVar(root)
str3 = StringVar(root)
str4 = StringVar(root)
str5 = StringVar(root)
str6 = StringVar(root)
str7 = StringVar(root)
str8 = StringVar(root)
str9 = StringVar(root)
button_config = {
    "width": 10,
    "height": 4,
    "font": ("Helvetica", 14)
}
x= 1
def clicked1():
    global x
    x = x + 1
    if x%2==0:
        str1.set("X")
    else:
       str1.set("O")
    winner()

def clicked2():
    global x
    x = x + 1
    if x % 2 == 0:
        str2.set("X")
    else:
        str2.set("O")
    winner()

def clicked3():
    global x
    x = x + 1
    if x % 2 == 0:
        str3.set("X")
    else:
        str3.set("O")
    winner()
def clicked4():
    global x
    x = x + 1
    if x % 2 == 0:
        str4.set("X")
    else:
        str4.set("O")
    winner()
def clicked5():
    global x
    x = x + 1
    if x % 2 == 0:
        str5.set("X")
    else:
        str5.set("O")
    winner()
def clicked6():
    global x
    x = x + 1
    if x % 2 == 0:
        str6.set("X")
    else:
        str6.set("O")
    winner()
def clicked7():
    global x
    x = x + 1
    if x % 2 == 0:
        str7.set("X")
    else:
        str7.set("O")
    winner()
def clicked8():
    global x
    x = x + 1
    if x % 2 == 0:
        str8.set("X")
    else:
        str8.set("O")
    winner()
def clicked9():
    global x
    x = x + 1
    if x % 2 == 0:
        str9.set("X")
    else:
        str9.set("O")
    winner()


def winner():
    global t
    if str1.get()=="X" and str2.get()== "X" and str3.get()== "X":
        messagebox.showinfo("Game Over", f"Player X wins!")
        t=10
        reset()
    elif str4.get() == "X" and str5.get() == "X" and str6.get() == "X":
        messagebox.showinfo("Game Over", f"Player X wins!")
        t = 10
        reset()
    elif str7.get() == "X" and str8.get() == "X" and str9.get() == "X":
        messagebox.showinfo("Game Over", f"Player X wins!")
        t = 10
        reset()
    elif str1.get()=="X" and str4.get()== "X" and str7.get()== "X":
        messagebox.showinfo("Game Over", f"Player X wins!")
        t = 10
        reset()
    elif str2.get()=="X" and str5.get()== "X" and str8.get()== "X":
        messagebox.showinfo("Game Over", f"Player X wins!")
        t = 10
        reset()
    elif str3.get()=="X" and str6.get()== "X" and str9.get()== "X":
        messagebox.showinfo("Game Over", f"Player X wins!")
        t = 10
        reset()
    elif str1.get() == "X" and str5.get() == "X" and str9.get() == "X":
        messagebox.showinfo("Game Over", f"Player X wins!")
        t = 10
        reset()
    elif str3.get() == "X" and str5.get() == "X" and str7.get() == "X":
        messagebox.showinfo("Game Over", f"Player X wins!")
        t = 10
        reset()

    if str1.get()=="O" and str2.get()== "O" and str3.get()== "O":
        messagebox.showinfo("Game Over", f"Player O wins!")
        t = 10
        reset()
    elif str4.get() == "O" and str5.get() == "O" and str6.get() == "O":
        messagebox.showinfo("Game Over", f"Player O wins!")
        t = 10
        reset()
    elif str7.get() == "O" and str8.get() == "O" and str9.get() == "O":
        messagebox.showinfo("Game Over", f"Player O wins!")
        t = 10
        reset()
    elif str1.get()=="O" and str4.get()== "O" and str7.get()== "O":
        messagebox.showinfo("Game Over", f"Player O wins!")
        t = 10
        reset()
    elif str2.get()=="O" and str5.get()== "O" and str8.get()== "O":
        messagebox.showinfo("Game Over", f"Player O wins!")
        t = 10
        reset()
    elif str3.get()=="O" and str6.get()== "O" and str9.get()== "O":
        messagebox.showinfo("Game Over", f"Player O wins!")
        t = 10
        reset()
    elif str1.get() == "O" and str5.get() == "O" and str9.get() == "O":
        messagebox.showinfo("Game Over", f"Player O wins!")
        t = 10
        reset()
    elif str3.get() == "O" and str5.get() == "O" and str7.get() == "O":
        messagebox.showinfo("Game Over", f"Player O wins!")
        t = 10
        reset()

    if x==10 and t==1:
        messagebox.showinfo("Game Over", f"Game Draw!")
        reset()
def reset():
    global x
    x = 0
    str1.set("")
    str2.set("")
    str3.set("")
    str4.set("")
    str5.set("")
    str6.set("")
    str7.set("")
    str8.set("")
    str9.set("")

buttons = []
row = []

btn =Button(root, text="", **button_config,command=clicked1,textvariable=str1)
btn.grid(row=1, column=1, padx=5, pady=5)
row.append(btn)
buttons.append(row)
btn =Button(root, text="", **button_config,command=clicked2,textvariable=str2)
btn.grid(row=1, column=2, padx=5, pady=5)
row.append(btn)
buttons.append(row)
btn =Button(root, text="", **button_config,command=clicked3,textvariable=str3)
btn.grid(row=1, column=3, padx=5, pady=5)
row.append(btn)
buttons.append(row)

btn =Button(root, text="", **button_config,command=clicked4,textvariable=str4)
btn.grid(row=2, column=1, padx=5, pady=5)
row.append(btn)
buttons.append(row)
btn =Button(root, text="", **button_config,command=clicked5,textvariable=str5)
btn.grid(row=2, column=2, padx=5, pady=5)
row.append(btn)
buttons.append(row)
btn =Button(root, text="", **button_config,command=clicked6,textvariable=str6)
btn.grid(row=2, column=3, padx=5, pady=5)
row.append(btn)
buttons.append(row)

btn =Button(root, text="", **button_config,command=clicked7,textvariable=str7)
btn.grid(row=3, column=1, padx=5, pady=5)
row.append(btn)
buttons.append(row)
btn =Button(root, text="", **button_config,command=clicked8,textvariable=str8)
btn.grid(row=3, column=2, padx=5, pady=5)
row.append(btn)
buttons.append(row)
btn =Button(root, text="", **button_config,command=clicked9,textvariable=str9)
btn.grid(row=3, column=3, padx=5, pady=5)
row.append(btn)
buttons.append(row)


root.mainloop()