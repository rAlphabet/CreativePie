import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit
def julia(re, im, rec, imc, iteration, radius):
    c = complex(rec, imc)
    z = complex(re, im)
    for i in range(iteration):
        z = z**2 + c
        if z.real**2 + z.imag**2  >= radius:
            return i
    return iteration

def draw(cols, rows, iteration, radius, cmaper, rec, imc):
    result = np.zeros([rows, cols])
    for i, re in enumerate(np.linspace(-2, 2, num = rows)):
        for j, im in enumerate(np.linspace(-2, 2, num=cols)):
            result[i, j] = julia(re, im, rec, imc, iteration, radius)

    fig = plt.figure(frameon=False, dpi=100)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.imshow(result.T, cmap=cmaper, interpolation="bilinear",\
        extent=[-2, 2, -2, 2])
    plt.show()


draw(2400, 2400, 640, 4, "inferno", 0, 0.75)
draw(2400, 2400, 640, 4, "inferno", 0.4, 0.325)
draw(2400, 2400, 640, 4, "inferno", -0.293, -0.653)
draw(2400, 2400, 640, 4, "inferno", -0.8, 0.156)
draw(2400, 2400, 640, 4, "inferno", -0.7269, 0.1889)