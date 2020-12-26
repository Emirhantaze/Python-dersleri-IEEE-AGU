import matplotlib.pyplot as plt
import numpy as np

ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)
t = np.arange(0, 2, 0.001)
f1 = np.sin(2*np.pi*1*t)
f2 = np.sin(2*np.pi*3*t)
plt.sca(ax1)
plt.plot(t, f1)
plt.sca(ax2)
plt.plot(t, f2)

plt.show()
