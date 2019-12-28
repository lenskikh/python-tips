'''
Операции с canvas
'''
#-------------------------------------------

#Реакция на клавиатуру

from tkinter import Canvas,Tk,mainloop
window = Tk()

def callback(event):
    #перевод события в строку, чтобы можно разделить.
    razbor = str(event).split(" ")
    print(razbor)

canvas = Canvas(width=240, height=240, bg="white")

#Установление фокуса на фрейме. Автоматом фокус вне фрейма.
canvas.focus_set()

#реакция на любую клавишу
canvas.bind("<Key>", callback)
canvas.pack()
mainloop()

#-------------------------------------------

#показывает координаты нажатия мышки
from tkinter import Canvas,Tk,mainloop
window = Tk()

def callback(event):
    print(str(event.x) + "," + str(event.y))
    
canvas = Canvas(width=240, height=240, bg="white")

canvas.bind("<Button-1>", callback)
canvas.pack()
mainloop()

#-------------------------------------------

#загрузка изображения в canvas
import tkinter
window  = tkinter.Tk()

canvas = tkinter.Canvas(window , height=900, width=502)
canvas.grid(row = 0, column = 0)

calculator_background = tkinter.PhotoImage(file = 'images/bg.gif')
canvas.create_image(253,450, image=calculator_background)

canvas.pack()
window.mainloop()

#-------------------------------------------
