import turtle
import random

def make_rect(t, w, h):
    t.begin_fill()
    for i in range(2):
        t.fd(w)
        t.left(90)
        t.fd(h)
        t.left(90)
    t.end_fill()

def rect(t, x, y, width, height, color):
    t.up()
    t.goto(x - width/2, y - height/2)
    t.fillcolor(color)
    t.down()
    make_rect(t, width, height)

def draw(iteration):
    turtle.setup(720, 720)
    t = turtle.Pen()
    turtle.tracer(100, None)
    t.hideturtle()
    for i in range(iteration):
        rect(t, random.randint(-300, 300), random.randint(-300, 300),\
            random.randint(5, 100), random.randint(5, 100),\
                (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0,1)))
    turtle.done()

draw(500)