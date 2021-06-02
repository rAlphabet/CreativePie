import numpy as np
import matplotlib.pyplot as plt
import numba
import random

@numba.njit
def dejong(x, y, a, b, c, d):
    return (np.sin(a*y) - np.cos(b*x),
                np.sin(c*x) - np.cos(d*y))

@numba.njit
def make(a, b, c, d, iterations=600000):
    X = np.zeros(iterations)
    Y = np.zeros(iterations)
    for i in range(iterations):
        sols = dejong(X[i], Y[i], a, b, c, d)
        X[i+1] = sols[0]
        Y[i+1] = sols[1]
    print(a, b, c, d)
    return X, Y

def draw(X, Y, color):
    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.scatter(X, Y, s=0.0001, c=color)
    plt.show()

def randomparams():
    return [round(random.uniform(-np.pi, np.pi), 3) for i in range(4)]

colors = ["lightpink", "paleturquoise"]

# X, Y = make(0.97, -1.9, 1.38, -1.5)
# draw(X, Y, random.choice(colors))

# X, Y = make(1.4, -2.3, 2.4, -2.1)
# draw(X, Y, random.choice(colors))

# X, Y = make(-2.095, 1.536, 1.588, 2.034)
# draw(X, Y, random.choice(colors))

# X, Y = make(2.89, -2.071, 1.664, 2.159)
# draw(X, Y, random.choice(colors))

# # X, Y = make(-1.161, 1.394, -1.552, 1.74)
# # draw(X, Y, random.choice(colors))

# X, Y = make(-1.044, -2.685, -1.376, 0.778)
# draw(X, Y, random.choice(colors))

a, b, c, d = randomparams()
X, Y = make(a, b, c, d)
draw(X, Y, random.choice(colors))