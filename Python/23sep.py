"""
collections in Python
special collections:
                                Mutable     Ordered
strings         characters          N           Y       
dictionaries    key:value pairs     Y           N

Normal Collections (General/Regular)
        Mutable     Ordered
lists       Y           Y
tuples      N           Y
sets        Y           N
frozensets  N           N
"""
# tuples:   Immutable & Ordered collections of members.
"""
tp1 = (22,66,0,44,12,-45, 0, 11, 0)
# in:  0  1  2  3  4  5
print(tp1)
print(type(tp1))
print(len(tp1))
print(max(tp1))
print(min(tp1))
print(sorted(tp1))
tp1_sorted = tuple(sorted(tp1))
print(tp1[1])
print(tp1[-2])
print(tp1[1:-2:2])

# tp1[2] = 333      tuples are immutable.
print(tp1.count(0))
# print(tp1.count(0, 2, 4))     not available in tuples
print(tp1.index(12))
print(tp1.index(0, 7))
print(tp1.index(0, 4, 7))
print(tp1.index(10, 4, 7))
"""

# Defining a single element tuple
# tp2 = (117)
# tp3 = ("Lion")
# tp2 = (117,)
# tp3 = ("Lion",)
# print(tp2, type(tp2))
# print(tp3, type(tp3))

# Another way to define a tuple
tp1 = 22, 66, 0, 44, 12, -45, 0, 11, 0
print(tp1)
print(type(tp1))
tp2 = 117,
print(tp2)
print(type(tp2))
list1 = list(tp1)
list1.pop(6)
list1.pop(7)
tp1 = tuple(list1)
print(tp1)

del tp1