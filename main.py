from tkinter import *
from math import *

width = 500
height = 500
scale = 30
line_x = width // 2
line_y = height // 2
x_min, x_max = -3, 3
y_min, y_max = -2, 2

def draw_axes():
    draw_button.destroy()
    canvas.create_line(0, line_y, width, line_y, fill="black")
    canvas.create_line(line_x, 0, line_x, height, fill="black")

    for i in range(x_min, x_max + 1):
        current_x = line_x + i * scale
        canvas.create_line(current_x, line_y - 5, current_x, line_y + 5, fill="gray")
        canvas.create_text(current_x + 2, line_y + 8, text=str(i), anchor=NW)

    for i in range(y_min, y_max + 1):
        if i == 0:
            continue
        current_y = line_y - i * scale
        canvas.create_line(line_x - 5, current_y, line_x + 5, current_y, fill="gray")
        canvas.create_text(line_x + 8, current_y - 8, text=str(i), anchor=NW)

    plot_function(canvas)

def plot_function(canvas):
    prev_x = None
    prev_y = None
    x = x_min
    while x <= x_max:
        y = sin(x) + cos(x)
        canvas_x = line_x + x * scale
        canvas_y = line_y - y * scale
        if prev_x is not None and prev_y is not None:
            canvas.create_line(prev_x, prev_y, canvas_x, canvas_y, fill="red")
        prev_x = canvas_x
        prev_y = canvas_y
        x += 1 / scale

root = Tk()
root.title("График функции y = sin(x) + cos(x)")
root.geometry(f'{width}x{height}+500+150')
root.iconbitmap(default="./function.ico")

canvas = Canvas(root, width=width, height=height, bg="light blue")
canvas.pack()

draw_button = Button(text="Давайте рисовать!", command=draw_axes)
draw_button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
