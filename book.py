'''
Python - поварная книга.
Пишется для новичков, поэтому код приводится полностью для каждого случая.

* Реакция на клавиатуру
* Показывает координаты нажатия мышки
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
