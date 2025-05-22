from tkinter import *
ryan_root=Tk()
ryan_root.geometry("1000x1000")

canvas_width=800
canvas_height=400

ryan_root.geometry(f"{canvas_width}x{canvas_height}")
can_widgt=Canvas(ryan_root,width=canvas_width,height=canvas_height)
can_widgt.pack()
# the line goes from x1,y1 to x2,y2
can_widgt.create_line(0,0,canvas_width,canvas_height)

# top left to bottom right
can_widgt.create_rectangle(2,10,500,400)

can_widgt.create_text(100,100,text="HI")

can_widgt.create_oval(100,100,200,200)

can_widgt.create_arc(100,900,200,200,start=0,extent=180)

can_widgt.create_polygon(00,100,200,200,300,100)

can_widgt.create_bitmap(200,300,bitmap="info")

can_widgt.create_window(200,150,window=Label(ryan_root,text="hi"))
# can_widgt.create_image(400,300,image=PhotoImage(file="C:/Users/George/PycharmProjects/pythonProject1/images/python.png"))
# btn = Button(can_widgt, text="Click Me")
# can_widgt.create_window(200, 200, window=btn)
ryan_root.mainloop()