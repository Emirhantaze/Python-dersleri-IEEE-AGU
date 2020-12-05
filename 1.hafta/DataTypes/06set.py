#       Set

# unique elements and unordered
# fast reach and add

s1 = set()

s2 = {3, 5, 7, 9, 6}

s2.add(12)
s2.remove(12)

s2.clear()
s2.copy()

s2.discard() #remove if not exist do nothing

s2.issubset(s1)
s2.issuperset(s1)

s1.difference(s2)
s1 - s2

s1.union(s2)
s1 | s2

s1.intersection(s2)
s1 & s2

s1.symetric_difference(s2)
s1 ^ s2


# frozen set immutable version of sets