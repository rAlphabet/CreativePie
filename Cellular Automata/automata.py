import numpy as np
import matplotlib.pyplot as plt
import numba

p = np.array([0, 1, 1, 1, 1, 0, 0, 0])

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

def draw(n, p, cmaper):
    plt.matshow(automata(n, p), cmap = cmaper)
    plt.axis("off")
    plt.show()

draw(64, p, "Greys")
draw(128, p, "Greys")
draw(256, p, "Greys")
draw(360, p, "Greys")