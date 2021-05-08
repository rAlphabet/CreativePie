import turtle
import os

def star(t, angle, side, limit, turningPoint = 200):
    t.forward(side)
    if side % (turningPoint*2) == 0:
        angle += 2
    elif side % turningPoint == 0:
        angle -= 2

    t.right(angle)
    side += 2

    if side < limit:
        star(t, angle, side, limit)

def draw(angle, side, limit, turningPoint = 200, save = False, filename = None):
    window = turtle.Screen()
    window.bgcolor("black")
    t = turtle.Turtle()
    t.pencolor("white")
    t.width(1)
    turtle.tracer(100, None)
    star(t, angle, side, limit, turningPoint)
    if save and filename != None:
        path = os.getcwd() + r"\\"
        cv = turtle.getscreen().getcanvas()
        cv.postscript(file = path + filename + ".ps", colormode="color")
    turtle.clearscreen()

for i in [119, 120, 121, 110, 135, 140, 180]:
    draw(i, 0, 1200, 200, save=True, filename=f"star{i}")