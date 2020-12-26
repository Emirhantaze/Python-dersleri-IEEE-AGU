import numpy as np

arr = np.array([[1, 2], [3, 4], [1, 2]], dtype="int16")
print(np.shape(arr))
#  shape
#  (8,)
# [1,2,3] size = 3
# [[1,2],[3,4],[1,2]] size = 6 size = 3 , size = 2


arr = np.zeros((4, 5), dtype=int)
print(arr)
arr = np.reshape(arr, (10, 2))
print(arr)
a = np.empty((10,))
print(a)
# print(a)
# np.shape()
# np.reshape()
# print()
# np.linspace(0,100,10000)
# np.abs()
# np.arange(0,10,0.1)
# np.nonzero(arr == 1)
# np.where()
