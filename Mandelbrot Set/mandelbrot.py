import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit
def mandelbrot(re, im, iteration, radius):
    c = complex(re, im)
    z = 0.0j
    for i in range(iteration):
        z = z**2 + c
        if z.real**2 + z.imag**2  >= radius:
            return i
    return iteration

def draw(cols, rows, iteration, radius, cmaper):
    result = np.zeros([rows, cols])
    for i, re in enumerate(np.linspace(-2, 1, num = rows)):
        for j, im in enumerate(np.linspace(-1, 1, num=cols)):
            result[i, j] = mandelbrot(re, im, iteration, radius)

    fig = plt.figure(frameon=False, dpi=100)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.imshow(result.T, cmap=cmaper, interpolation="bilinear",\
        extent=[-2, 1, -1, 1])
    plt.show()

draw(1024, 1024, 13, 4, "bone")
draw(1024, 1024, 100, 4, "inferno")