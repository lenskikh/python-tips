'''
Операции с canvas
'''
#-------------------------------------------

#Реакция на нажатия с клавиатуры

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

#движение объекта после нажатия мышкой
import tkinter
window  = tkinter.Tk()

def callback(event):
    #движение на 5 пикселей по оси х
    canvas.move(id, 5,0) 
    
canvas = tkinter.Canvas(window , height=500, width=500)
canvas.grid(row = 0, column = 0)

man = tkinter.PhotoImage(file = 'images/pixel-man.gif')
id = canvas.create_image(253,450, image=man)

canvas.bind("<Button-1>", callback)
canvas.pack()
window.mainloop()

#-------------------------------------------

#движения объекта с использованием стрелок
import tkinter
window  = tkinter.Tk()

def callback(event):
    #перевод события в строку, чтобы можно разделить.
    razbor = str(event).split(" ")
    arrows = razbor[4].split("=")[1]
    print(arrows)
    match arrows:
        case "Right":
            canvas.move(id, 5,0)
        case "Left":
            canvas.move(id, -5,0)
        case "Down":
            canvas.move(id, 0,5)
        case "Up":
            canvas.move(id, 0,-5)     
 
canvas = tkinter.Canvas(window , height=500, width=500)
canvas.grid(row = 0, column = 0)

man = tkinter.PhotoImage(file = 'images/pixel-man.gif')
id = canvas.create_image(15,30, image=man)

#Установление фокуса на фрейме. Автоматом фокус вне фрейма.
canvas.focus_set()

#реакция на любую клавишу
canvas.bind("<Key>", callback)

canvas.pack()
window.mainloop()

#-------------------------------------------

#рисует квардраты по курсору мышки.
import tkinter
window  = tkinter.Tk()

def callback(event):
    print(str(event.x) + "," + str(event.y))
    canvas.create_rectangle(event.x,event.y,event.x+8,event.y+8, fill="black")
    
canvas = tkinter.Canvas(window , height=500, width=500)
canvas.grid(row = 0, column = 0)

canvas.bind("<Button-1>", callback)
canvas.pack()
window.mainloop()

#-------------------------------------------

#Получение id объекта по нажатию мышы
import tkinter as tk

def get_object_id(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    item_id = canvas.find_closest(x, y)[0]
    print("Clicked object ID:", item_id)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create some objects on the canvas
rect_id = canvas.create_rectangle(50, 50, 150, 150, fill="red")
oval_id = canvas.create_oval(200, 200, 300, 300, fill="blue")

# Bind the function to the mouse click event
canvas.bind("<Button-1>", get_object_id)

root.mainloop()

#-------------------------------------------

#Удаление объекта по id
import tkinter as tk

# Create the main window
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Create an example object and get its ID
object_id = canvas.create_rectangle(50, 50, 150, 150, fill='blue')

# Function to delete the object by its ID
def delete_object_by_id(canvas, object_id):
    canvas.delete(object_id)

# Delete the object
delete_object_by_id(canvas, object_id)

root.mainloop()

#-------------------------------------------

#решаем проблему с созданием множеством объектов
import tkinter as tk

# Создаем главное окно
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Глобальная переменная для хранения изображения
img_objects = []

def create_obj(x, y, figure):
    obj = tk.PhotoImage(file=figure)
    canvas.create_image(x, y, image=obj)
    img_objects.append(obj)  # Сохраняем ссылку на изображение

# Создание объекта изображения
create_obj(105, 555, 'pawn_white.png')

root.mainloop()

