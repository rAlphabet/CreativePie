import matplotlib.pyplot as plt
import numpy as np
import random
import mplcyberpunk

data = np.linspace(0, np.pi, 1000)

def heartbeat(data, life = True):
    alive = [i + random.uniform(-0.01, 0.01)
             if -0.1 < i < 0.1 and k % 10 == 0 else i for k, i in
              enumerate(8*np.sin(data + 1.5) * np.sin(data)**63)]
    dead = [0] * len(data)
    return alive if life else dead

def draw(data, response, color):
    plt.style.use("cyberpunk")
    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.plot(data, response, c=color)
    ax.scatter(data[-1], response[-1], s=40 ,c=color)
    mplcyberpunk.make_lines_glow()
    plt.show()

draw(data, heartbeat(data), "lightblue")
draw(data, heartbeat(data, life=False), "lightblue")