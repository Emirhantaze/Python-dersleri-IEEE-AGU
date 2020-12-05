####        List

A = [3, 4, 5, 6, 11, 15]
B = list()

# reach and modify

A[0]
A[1] = 18

A[-1]

A[2:4]
A[:-3]
A[::2]
A[2:4] = [11, 19, 35, 46]

A[:] = [] #clear
del A[0]

# functions
A.append(12)
A.extend([4, 5, 9]) #iterable
A.insert(0, 15) # ! O(n)
A.remove(3) # removes first 3 on the list
A.pop() # optional to give i
A.count(3)
A.reverse()
A.copy() # = A[:]

A.sort()
A.sort(reverse=True)

A.sort(key=lambda x:x)


# queue
from collections import deque
queue = deque(["Eric", "John", "Micheal"])
queue.popleft()

