import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

ax = plt.gca()


def anime(i):
    # ax.cla()
    t = np.arange(0+i/10, 2+i/10, 0.01)
    f = np.sin(2*np.pi*2*t)
    ax.plot(t, f, color="b")


a = FuncAnimation(plt.gcf(), anime, range(100), interval=100, repeat=False)

plt.show()
