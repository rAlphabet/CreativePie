import turtle
import math
import os
import random

def fill_canvas(t, n, color):
	t.pensize(3)
	t.color(color)
	t.begin_fill()
	for j in range(4):
		for i in range(4):
			t.forward(n)
			t.left(90)
		t.left(90)
	t.end_fill()

def spiral(t, size, scale = 1, rnd = False):
	for i in range(size):
		t.forward(math.sqrt(i) / scale)
		t.left(i % 180)
		if rnd:
			t.left(random.randint(-1, 1))

def draw(size, scale = 1, rnd = False, save = False, filename = False):
	window = turtle.Screen()
	window.bgcolor("white")
	t = turtle.Pen()
	turtle.tracer(100, None)
	fill_canvas(t, 500, "light blue")
	t.pencolor("black")
	t.pensize(1)
	spiral(t, size, scale, rnd)
	if save and filename != None:
		path = os.getcwd() + r"\\"
		cv = turtle.getscreen().getcanvas()
		cv.postscript(file = path + filename + ".ps", colormode="color")
	turtle.clearscreen()

draw(1637, scale=1.5, save=True, filename="spiral")

for i in range(1, 11):
	draw(2000, scale=1.5, rnd=True, save=True, filename=f"spiral{i}")