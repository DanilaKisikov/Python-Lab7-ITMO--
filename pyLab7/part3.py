import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np


if __name__ == "__main__":
    x = np.linspace(-np.pi, np.pi, 1000)
    y = np.multiply(np.sin(x), np.cos(x))
    z = np.sin(x)

    fmt = ScalarFormatter()
    fmt.set_powerlimits((-3, 3))

    graph = plt.figure(figsize=(6, 4))
    ax = graph.add_subplot(111, projection='3d')
    ax.plot(xs=x, ys=y, zs=z, marker='x', color='red')

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_xlim([-np.pi, np.pi])
    ax.set_ylim([-np.pi, np.pi])
    ax.set_zlim([-np.pi, np.pi])

    plt.gca().xaxis.set_major_formatter(fmt)

    plt.show()

