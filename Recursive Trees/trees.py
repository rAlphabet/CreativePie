import os
import turtle
import random

colors = ["#228B22", "#008000", "#006400", "#808000", "#556B2F", "#6B8E23"]

def recursive_tree(t, length, angle, scale, density):
    if length < density:
        return None
    t.color(random.choice(colors))
    t.forward(length)
    t.left(angle)
    recursive_tree(t, length * scale, angle, scale, density)
    t.right(2*angle)
    recursive_tree(t, length * scale, angle, scale, density)
    t.left(angle + 180)
    t.forward(length)
    t.left(180)

def draw(length, angle, scale, density, move=200, save = False, filename = None):
    window = turtle.Screen()
    window.bgcolor("light blue")
    turtle.tracer(100, None)
    t = turtle.Pen()
    t.color("dark green")
    t.pensize(1)
    t.left(90)
    t.backward(move)
    recursive_tree(t, length, angle, scale, density)
    t.hideturtle()
    if save and filename != None:
        path = os.getcwd() + r"\\"
        cv = turtle.getscreen().getcanvas()
        cv.postscript(file = path + filename + ".ps", colormode='color')
    turtle.clearscreen()

draw(100, 25, 0.8, 5, save=True, filename="normal")
draw(100, 37, 0.8, 3, save=True, filename="dense")
draw(100, 15, 0.8, 5, save=True, filename="tall")
draw(100, 90, 0.8, 3, save=True, move=100, filename="square")