import random
import matplotlib.pyplot as plt

def nums(iteration):
    num = {"x": [], "y": []}
    for i in range(iteration):
        num["x"] += [random.uniform(0, 1)]
        num["y"] += [random.uniform(0, 1)]
    return num

def draw(num):
    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.plot([*set(num["x"])], [*set(num["y"])], ",", color="grey")
    ax.plot(num["x"], num["y"], ",", color="dimgrey")
    ax.plot(num["x"], [*set(num["y"])], ",", color="white")
    plt.show()

draw(nums(100000))