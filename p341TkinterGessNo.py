from tkinter import *
import random

def check_guess():
        user_guess = int(txtno1.get())
        if user_guess == a:
            result_label.config(text="You are right!")
        else:
            result_label.config(text="You are wrong!")


root = Tk()
root.geometry("250x150")
root.title("Guess the Number")

a = random.randint(1, 50)
print("Random number (for testing):", a)

Label(root, text="Enter a number between 1 and 50:").grid(row=0, column=0, columnspan=2, pady=10)

txtno1 = Entry(root)
txtno1.grid(row=1, column=0, columnspan=2)

Button(root, text="Check", command=check_guess).grid(row=2, column=0, columnspan=2, pady=10)

result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
