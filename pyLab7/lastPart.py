import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter, FuncAnimation, MovieWriter
import math

pointsCount = 60
step = 2 * np.pi / (pointsCount * 0.5)
pi = np.pi


def save(fps, animation):
    writer = PillowWriter(fps=fps)

    f = r"myAnimation.gif"

    animation.save(f, writer=writer)


def anim(i):
    lastX = -pi + i * step
    lastY = math.sin(lastX)

    ax.plot(lastX, lastY, color='blue', label='original', marker='o')

    if i < pointsCount:
        ax.set_xlim([-4, 4])
    else:
        leftCorner = -4 - 2*pi + step * i
        rightCorner = 4 - 2*pi + step * i
        ax.set_xlim([leftCorner, rightCorner])

    ax.set_ylim([-1.5, 1.5])


def anim1(i):
    ax.clear()
    thisStep = i * step
    lastX = pi + thisStep
    firstX = -4 + thisStep

    diff = 4 - pi

    x = np.linspace(firstX, lastX, pointsCount)
    y = np.sin(x)

    ax.plot(x, y, color='blue')

    leftCorner = firstX
    rightCorner = lastX + diff
    ax.set_xlim([leftCorner, rightCorner])


if __name__ == '__main__':
    fig = plt.figure(figsize=(8, 3))
    ax = fig.add_subplot()

    animation = FuncAnimation(fig, anim1, frames=pointsCount*4, interval=16, repeat=True)

    #plt.show()

    save(30, animation)
