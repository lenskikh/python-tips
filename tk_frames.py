from tkinter import *

root = Tk()
frame1 = Frame(root, width=100, height=100, background="bisque")
frame2 = Frame(root, width=50, height = 50, background="#b22222")
frame3 = Frame(root, width=50, height = 50, background="green")

frame1.place(x=0,y=0)
frame2.place(x=0,y=100)
frame3.place(x=50,y=100)

root.mainloop()
