# Strings: ordered & immutable collections of characters
# string1 = "Jaypal is a good boy."
# index no:0123456789..........20
# -ve ind:21...........987654321
"""
string2 = 'Jaypal is really a good boy.'
print(string1[5])
print(string1)
print(type(string1))
print(len(string1))

# Slicing
print(string1[3:15])
print(string1)      # Slicing never changes the original data
# print(string1[1582])
print(string1[3 : 1582])
print(string1[3 : ])
print(string1[ : 15])
print(string1[ : ])
s3 = string1[3 : 15]
print(s3)
# string1 = string1[3 : 15]
# print(string1)

print(string1[2:19:2])
print(string1[2:19:1582])
print(string1[12])
print(string1[-9])
print(string1[5 : -8])
print(string1[-18 : -6])
print(string1[-3 : -15])
print(string1)

print(string1[::3])
print(string1[::-1])
print(string1[-3 : -15 : -1])
print(string1[-3 : -15 : -3])

# defaults: string1[0th index:length of string:1])

s3 = "9428128473"
print(max(s3))
print(min(s3))
print(sorted(s3))       # sorted always returns you a list

print(max(string1))
print(min(string1))
print(sorted(string1))
"""
# String Methods - functions vs. methods
# None of the string method changes the original string as they are immutable. They simply return a copy of the original string with changes.
s1 = "It's fun to learn Python."
print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())
s2 = "Miß"
print(s2.casefold())
print(s2.lower())
print(s2.upper())

print(s1.center(100))
print(s1.center(100, "*"))
print(s1.count(" "))
print(s1.count("ea"))
print(s1.count("boy"))
print(s1.count("o", 10, 20))
print(s1.count("o", 10))

s2 = "My vulgar fraction is: ⅛"
print(s2.encode())
print(s1.endswith("."))
print(s1.endswith("Python"))
print(s1.endswith("learn", 0, 17))
print(s1.startswith("learn", 12))

s3 = "I\thave\ta\tnice\tfamily"
print(s3)
print(s3.expandtabs(16))