s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {2,3,4,5,7,9,8,6}
s4 = s1.union(s2)
s5 = {5,6,7,8}
print(s1)
print(s4)
print(s1.intersection(s2))
print(s1.difference(s2))       # s1 - s2
print(s2.difference(s1))       # s2 - s1
print(s1.symmetric_difference(s2))     # (s1 - s2)U(s2 - s1)
print(s1)
# s1 = s1.symmetric_difference(s2)
# s1.symmetric_difference_update(s2)
# s2.symmetric_difference_update(s1)
# s1.difference_update(s2)
# s1.intersection_update(s2)
# s1.update(s2)
print(s1)
# s1.intersection(s5)
print(s1.isdisjoint(s5))
print(s2.isdisjoint(s5))
print(s1.issubset(s3))
print(s2.issubset(s3))
print(s3.issuperset(s2))
"""
special collections:
                Mutable     Ordered
string          N           Y
dictionary      Y           N

Collections     Mutable     Ordered
list            Y           Y
tuple           N           Y
set             Y           N
forzenset       N           N
"""

# Frozensets: Unordered & Immutable collection of members in which repeatition is eliminated. It is just a version of sets that is immutable.
fz1 = frozenset([1,2,3,4])
print(fz1)
print(type(fz1))
fz2 = frozenset([1,2,3,4,4,4])
print(fz2)