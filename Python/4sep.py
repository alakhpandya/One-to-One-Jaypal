# Lists: Ordered & Mutable collection of members/elements
"""
list1 = [12, 15, -22, 34.7, 0]
# index: 0   1     2    3   4
#-ve ind:-5  -4   -3   -2  -1
print(list1[2])
print(list1[-2])
print(list1)
print(type(list1))
print(len(list1))
print(max(list1))
print(min(list1))
print(sorted(list1))
print(list1)

vegetables = ["spinach", "onion", "garlic", "tomato", "Potato"]
print(max(vegetables))
print(min(vegetables))

mix_veg = ["spinach", 1, "onion", 2, "garlic", 0.5, "tomato", -1, "potato", 0]
print(mix_veg)
mix_veg2 = ["spinach", "1", "onion", "2", "garlic", "0.5", "tomato", "-1", "potato", "0"]

print(max(mix_veg2))
print(min(mix_veg2))
print(sorted(mix_veg2))

numbers = [22, 11, 34, 88, -65, 993, 22, -43, 0, 22, 34]
numbers[3] = 99
print(numbers)
print(numbers[2:8])
print(numbers[2:10:2])
print(numbers[-10:-1:2])
print(numbers[10:2:-2])
"""
# List methods
numbers = [22, 11, 34, 88, -65, 993, 22, -43, 0, 22, 34]
numbers.append(9)
x = 15
print(numbers.append(x))        # Most of list methods do not return anything
print(numbers)
# numbers.append()
# print(numbers)
# numbers.clear()
# print(numbers)
# del numbers
# print(numbers)

# n2 = numbers
# print(n2)
# n2.append(-482)

# n3 = numbers.copy()
# del numbers
# print(n2)
# del n2
# print(n3)

print(numbers.count(22))
# print(numbers.count(22, 1, 7))    Not allowed!
y = [19, 20]
numbers.extend(y)
print(numbers)

print(numbers.index(88))
print(numbers.index(22, 2, 10))

numbers.insert(4, 0)
print(numbers)

print(numbers.pop(4))
print(numbers)

numbers.remove(-65)
print(numbers)

# numbers.reverse()
# print(numbers)

numbers.sort()
print(numbers)

p = 13
q = str(p)
s1 = "Jaypal"
l1 = list(s1)
print(l1)
s2 = str(l1)
print(s2)
s3 = "".join(l1)
print(s3)
# Next Lecture: Operators