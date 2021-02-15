import os
import turtle
import random
import numpy as np

def planet(t, distance, rotation, turningPoint, limit):
    t.backward(limit)
    t.right(90)
    t.begin_fill()
    t.circle(limit)
    t.end_fill()
    t.pencolor("green")
    for i in range(distance):
        if i % turningPoint == 0:
            angle = random.randint(-rotation, rotation)
        t.left(angle)
        if np.sqrt(t.xcor()**2 + t.ycor()**2) >= limit:
            t.left(180)
            t.forward(1)
        t.forward(random.uniform(0, 1))

def draw(distance, rotation = 40, turningPoint = 25, limit = 200, save = False, filename = None):
    window = turtle.Screen()
    window.bgcolor("black")
    t = turtle.Pen()
    turtle.tracer(250, None)
    t.pencolor("blue")
    t.fillcolor("blue")
    t.pensize(8)
    planet(t, distance, rotation, turningPoint, limit)
    if save and filename != None:
        path = os.getcwd() + r"\\"
        cv = turtle.getscreen().getcanvas()
        cv.postscript(file = path + filename + ".ps", colormode="color")
    turtle.clearscreen()

for i in range(1, 11):
    draw(300000, save=True, filename=f"planet{i}")