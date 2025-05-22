from tkinter import *

ryan_root = Tk()
ryan_root.geometry("500x500")

def getvals():
    print(f"{namevalue.get()}, {phonevalue.get()}, {foodservicevalue.get()}")
    with open("1Records.txt", "a") as f:
        f.write(f"{namevalue.get()}, {phonevalue.get()}, {foodservicevalue.get()}\n")

# Title
Label(ryan_root, text="Ryan's GUI", font="comicsansms 13 bold").grid()

# Labels
name = Label(ryan_root, text="Name")
phone = Label(ryan_root, text="Phone")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)

# Entry variables
namevalue = StringVar()
phonevalue = StringVar()
foodservicevalue = IntVar()  # Make sure this is a separate variable

# Entry boxes
name_entry = Entry(ryan_root, textvariable=namevalue)
phone_entry = Entry(ryan_root, textvariable=phonevalue)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)

# Checkbox
foodservice = Checkbutton(text="Food Service", variable=foodservicevalue)
foodservice.grid(row=3, column=3)

# Button
Button(text="Submit", command=getvals).grid(row=4, column=3)

ryan_root.mainloop()
