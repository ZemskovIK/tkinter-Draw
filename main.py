from tkinter import *
from math import *

width = 600
height = 600
scale = 50
line_x = width // 2
line_y = height // 2
x_min, x_max = -5, 5
y_min, y_max = -5, 5

def draw_axes():
    canvas.delete("all")
    
    function_text = function_entry.get()
    title_label.config(text=f"y = {function_text}")
    
    canvas.create_line(0, line_y, width-5, line_y, fill="black", width=2)
    canvas.create_line(line_x, 5, line_x, height, fill="black", width=2)

    arrow_size = 10
    canvas.create_line(width-5, line_y, width-arrow_size-5, line_y-arrow_size, fill="black", width=2)
    canvas.create_line(width-5, line_y, width-arrow_size-5, line_y+arrow_size, fill="black", width=2)
    canvas.create_line(line_x, 5, line_x-arrow_size, arrow_size+5, fill="black", width=2)
    canvas.create_line(line_x, 5, line_x+arrow_size, arrow_size+5, fill="black", width=2)
    
    canvas.create_text(width-15, line_y-10, text="x", anchor=SE, font=("Arial", 12))
    canvas.create_text(line_x+10, 15, text="y", anchor=NW, font=("Arial", 12))

    for i in range(x_min, x_max + 1):
        if i == 0: continue
        current_x = line_x + i * scale
        canvas.create_line(current_x, 0, current_x, height, fill="lightgray", dash=(2,2))
        canvas.create_line(current_x, line_y - 5, current_x, line_y + 5, fill="black")
        canvas.create_text(current_x, line_y + 10, text=str(i), anchor=N, font=("Arial", 8))

    for i in range(y_min, y_max + 1):
        if i == 0: continue
        current_y = line_y - i * scale
        canvas.create_line(0, current_y, width, current_y, fill="lightgray", dash=(2,2))
        canvas.create_line(line_x - 5, current_y, line_x + 5, current_y, fill="black")
        canvas.create_text(line_x + 10, current_y, text=str(i), anchor=W, font=("Arial", 8))
    
    canvas.create_text(line_x + 10, line_y + 10, text="0", anchor=NW, font=("Arial", 8))

    plot_function()

def plot_function():
    function_text = function_entry.get()
    
    try:
        math_functions = {
            'sin': sin, 'cos': cos, 'tan': tan,
            'asin': asin, 'acos': acos, 'atan': atan,
            'sinh': sinh, 'cosh': cosh, 'tanh': tanh,
            'sqrt': sqrt, 'log': log, 'log10': log10,
            'exp': exp, 'abs': abs, 'round': round,
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
                    canvas.create_line(prev_x, prev_y, canvas_x, canvas_y, 
                                       fill="red", width=2, smooth=True)
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

Label(control_frame, text="Введите функцию: y = ").pack(side=LEFT)
function_entry = Entry(control_frame, width=30)
function_entry.insert(0, "sin(x) + cos(x)")
function_entry.pack(side=LEFT, padx=5)

draw_button = Button(control_frame, text="Построить график", command=draw_axes)
draw_button.pack(side=LEFT)

error_label = Label(root, text="", fg="red")
error_label.pack()

canvas = Canvas(root, width=width, height=height, bg="white")
canvas.pack()

root.mainloop()