import random
import matplotlib.pyplot as plt

X, Y = [0], [0]

def point(x, y, num):
    global X, Y
    if num == 0:
        X, Y = X + [x / 2], Y + [y / 2]
    elif num == 1:
        X, Y = X + [(x + 1) / 2], Y + [y / 2]
    else:
        X, Y = X + [(x + 0.5) / 2], Y + [(y + (3**0.5)) / 2]

def draw(iteration, scat = True):
    for i in range(iteration):
        point(X[-1], Y[-1], random.randint(0, 2))

    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.plot(X, Y, "w,") if scat else ax.plot(X, Y, "w")
    plt.show()

draw(80, scat=False)
draw(100000)