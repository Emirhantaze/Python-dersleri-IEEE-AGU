import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 2, 0.001)
f = np.sin(2*np.pi*10*t)
plt.subplot(1, 2, 1)
plt.plot(t, f, label="10 hz sine")
f = f + 1


plt.subplot(1, 2, 2)

plt.plot(t, f, label="10 hz sine + 1 ")
plt.legend()
plt.xlabel("saniye")
plt.ylabel("volt")
plt.title("sinusler")
plt.show()
