# sets: sets are mutable & unordered collections of members in which repeatition is eliminated.
# set1 = {1, 2, 3, 4, 5}
"""
print(set1, type(set1))
print(len(set1))
print(min(set1))
print(max(set1))
print(sorted(set1))
# print(set1[1])
# set1[2] = 24
# Creating an empty set
# set2 = {}     Creates empty DICTIONARY
set2 = set()
print(len(set2))
print(set2)
print(type(set2))

set3 = set("Jaypal Patel")
print(set3)
list2 = list(set3)
print(list2)
"""
# set methods:
"""
1. Regular Methods
2. Mathematical Set Operations

set1.add(6)
set1.add(6)
set1.add(6)
print(set1)
# set1.clear()
# print(set1)
# del set1
# print(set1)

set2 = set1.copy()
set1.discard(3)
set1.discard(3)
print(set1)
set1.remove(5)
# set1.remove(5)
print(set1)
print(set1.pop())
print(set1)

set3 = {13, 15, 19, 23}
print(set1.update(set3))
print(set1)
"""