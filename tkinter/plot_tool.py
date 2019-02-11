# Instagram: Phika.ir
# thanks to Java2s

from tkinter import *
import math

root = Tk()

frame = Frame(root)
Label(frame, text='f(x):').pack(side=LEFT)
func = Entry(frame)
func.pack(side=LEFT, fill=BOTH, expand=2)
butt = Button(frame, text='Plot')
butt.pack(side=RIGHT)
frame.pack(side=TOP)

frame = Frame(root)
bounds = []

for label in 'minX', 'maxX', 'minY', 'maxY':
    Label(frame, text=label + ':').pack(side=LEFT)
    edit = Entry(frame, width=10)
    edit.pack(side=LEFT)
    bounds.append(edit)
frame.pack(side=TOP)

c = Canvas(root)
c.pack(side=TOP, fill=BOTH, expand=5)


def minimax(values=[0.0, 1.0, 0.0, 1.0]):
    for i in range(4):
        edit = bounds[i]
        try:
            values[i] = float(edit.get())
        except:
            pass
        edit.delete(0, END)
        edit.insert(END, '%.2f'%values[i])
    return values


def plot():
    minx, maxx, miny, maxy = minimax()

    f = func.get()
    f = compile(f, f, 'eval')

    CX = c.winfo_width()
    CY = c.winfo_height()

    coords = []
    for i in range(0, CX, 5):
        coords.append(i)
        x = minx + ((maxx-minx)*i)/CX
        y = eval(f, vars(math), {'x': x})
        j = CY*(y-miny)/(maxy-miny)
        coords.append(j)

    c.delete(ALL)
    c.create_line(*coords)


butt.config(command=plot)
f = 'sin(x) + cos(x)'
func.insert(END, f)
minimax([0.0, 10.0, -2.0, 2.0])

root.mainloop()
