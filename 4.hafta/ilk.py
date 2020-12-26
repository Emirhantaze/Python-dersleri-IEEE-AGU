import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 2, 0.001)
f = np.sin(2*np.pi*10*t)

plt.plot(t, f, label="10 hz sine")
plt.legend()

plt.show()
# """
# amaç ım 0.5 saniyeden 1.5 saniye ye kadar sinyali sıfır yapma

# """
for i in range(10):
    print(i)

selected = np.arange(int(.5/.003), int(1.5/0.001))

f[int(.5/.001): int(1.5/0.001)] = np.abs(f[int(.5/.001): int(1.5/0.001)])

plt.plot(t, f, label="10 hz sine")
plt.legend()

plt.show()
# 0,1,2,3,4,,5,6..... son index
#  ilk eleman 0 , 0
#   0 + 0.001 1
#   0.001 + 0.001 2
#   0.002 + 0.001 3
# *

# 5 den 10 a kadar olan elemanlarını istiyorum

t = np.arange(0, 2, 0.003)
f = np.sin(2*np.pi*10*t)
plt.plot(t, f, label="10 hz sine")
plt.legend()

plt.show()
print(int(0.999/.003))
# absolute
# imaginery
# cumsum
# difference
# numpy save
# numoy load
