import numpy as np
import matplotlib.pyplot as plt
import numba
from scipy import signal

p = np.array([0, 1, 1, 1, 1, 0, 0, 0])
kernel = np.array([[0,1,2,1,0], [1,2,3,2,1], [2,3,4,3,2], [1,2,3,2,1], [0,1,2,1,0]])

@numba.njit
def automata(n, p):
    s = np.zeros(n)
    s[n//2] = 1
    mat = [s]
    for k in range(n//2-1):
        s_nov = np.zeros(n)
        for i in range(n):
            s_nov[i] = p[int(4*s[(i + n - 1) % n] + 2*s[i] + s[(i + 1) % n])]
        s = s_nov
        mat.append(s)
    return mat

def average(s, kernel):
    arr = np.array(s)
    return signal.convolve2d(arr, kernel, boundary='wrap', mode='same')/kernel.sum()

def draw(n, p, cmaper):
    plt.matshow(average(automata(n, p), kernel), cmap = cmaper)
    plt.axis("off")
    plt.show()

draw(64, p, "PiYG")
draw(128, p, "ocean")
draw(256, p, "seismic")