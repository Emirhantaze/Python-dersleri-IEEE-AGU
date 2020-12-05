"""
85-100 A
70-84  B
60-69  C
50-60  D
0-50   F
"""



grade = 38
print("You got an ", end="")
if grade >= 85:
    print("A")
    print("Congrulations")
elif grade >=70:
    print("B")
elif grade >= 60:
    print("C")
elif grade >= 50:
    print("D")
else:
    print("F")
    print("Work harder")



"""
Are there more than 1 maximum
"""

ls = [3, 6, 9, 15, 5, 7, 9, 12, 15]

maxVal = max(ls)
maxValCnt = ls.count(maxVal)

if maxValCnt > 1:
    print(f"There are {maxValCnt} times {maxVal}")
else:
    print("There are only one {maxVal}")



class A:
    def __init__(self, a):
        self.a = a


l = [A(3), A(5), A(8)]

def f(x):
    return abs(x.a)



arr = [int(i) if i!='0' else 1 for i in input().split()]


l.sort(key = lambda x:x.a)