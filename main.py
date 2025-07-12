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
    draw_button.pack_forget()
    canvas.delete("all")
    
    function_text = function_entry.get()
    title_label.config(text=f"y = {function_text}")
    
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

    plot_function()

def plot_function():
    function_text = function_entry.get()
    
    try:
        math_functions = {
            'sin': sin, 'cos': cos, 'tan': tan,
            'sqrt': sqrt, 'log': log, 'exp': exp,
            'pi': pi, 'e': exp(1)
        }
        
        def f(x):
            try:
                expr = function_text.replace('^', '**')
                return eval(expr, {'__builtins__': None}, {**math_functions, 'x': x})
            except:
                return float('nan')
        
        prev_x = None
        prev_y = None
        x = x_min
        while x <= x_max:
            y = f(x)
            if not isnan(y):
                canvas_x = line_x + x * scale
                canvas_y = line_y - y * scale
                if prev_x is not None and prev_y is not None:
                    canvas.create_line(prev_x, prev_y, canvas_x, canvas_y, fill="red")
                prev_x = canvas_x
                prev_y = canvas_y
            x += 1 / scale
                
    except Exception as e:
        error_label.config(text=f"Ошибка: {str(e)}")

root = Tk()
root.title("График функции")
root.geometry(f'{width}x{height+50}+500+150')
root.iconbitmap(default="./function.ico")

title_frame = Frame(root)
title_frame.pack(pady=5)
title_label = Label(title_frame, text="y = ", font=("Arial", 10, "bold"), fg="blue")
title_label.pack()

control_frame = Frame(root)
control_frame.pack(pady=5)

Label(control_frame, text="y = ").pack(side=LEFT)
function_entry = Entry(control_frame, width=30)
function_entry.insert(0, "sin(x) + cos(x)")
function_entry.pack(side=LEFT, padx=5)

draw_button = Button(control_frame, text="Построить", command=draw_axes)
draw_button.pack(side=LEFT)

error_label = Label(root, text="", fg="red")
error_label.pack()

canvas = Canvas(root, width=width, height=height, bg="white")
canvas.pack()

draw_button = Button(root, text="Построить график", command=draw_axes)
draw_button.pack(pady=10)

root.mainloop()
