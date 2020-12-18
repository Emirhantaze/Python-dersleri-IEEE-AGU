import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#  shape nedir
# [1,2,3] size = 3
# [[1,2],[3,4],[1,2]] size = 6 size = 3 , size = 2

a = np.empty((10,), dtype=int)
print(a)
np.shape()
np.reshape()
print()

np.nonzero(arr == 1)
np.where()
