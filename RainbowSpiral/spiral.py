import turtle
import os

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

def spiral(t, size):
    for i in range(size):
        t.pencolor(colors[i % 6])
        t.width(i/100 + 1)
        t.forward(i)
        t.left(59)

def draw(size, save = False, filename = None):
    window = turtle.Screen()
    window.bgcolor("black")
    t = turtle.Pen()
    turtle.tracer(100, None)
    spiral(t, size)
    if save and filename != None:
        path = os.getcwd() + r"\\"
        cv = turtle.getscreen().getcanvas()
        cv.postscript(file = path + filename + ".ps", colormode="color")
    turtle.clearscreen()

draw(500, save=True, filename="spiral")