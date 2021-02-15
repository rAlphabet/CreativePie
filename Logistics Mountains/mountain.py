import random
import numpy as np
import matplotlib.pyplot as plt

def mountain(seed, n_skip, n_iter, step = 0.0001, r_min = 0, scaling = 0):
    def logistic(r, x, scaling):
        return r*x*(1 - x) + scaling*np.sin(2*np.pi*x)**2
    
    R = []
    X = []
    r_range = np.linspace(r_min, 4, int(1/step))

    for r in r_range:
        x = seed
        for i in range(n_iter + n_skip + 1):
            if i >= n_skip:
                R.append(r)
                X.append(x)
            x = logistic(r, x, scaling)

    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.plot(R, X, ls='', marker=',', color="black")
    plt.ylim(0, 1)
    plt.xlim(r_min, 4.25)
    plt.show()

mountain(0.2, 1000, 10, r_min=2.98)
mountain(0.2, 1000, 10, r_min=2.98, scaling=0.1)
mountain(0.2, 1000, 10, r_min=2.98, scaling=0.05)