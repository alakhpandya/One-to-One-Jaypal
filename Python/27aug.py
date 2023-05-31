
s1 = "It's fun to learn Python."
"""
print(len(s1))
print(s1.find("l"))
print(s1.find("n"))
print(s1.find("n", 8))
print(s1.find("n", 17, 24))
print(s1.find("learn"))

print(s1.index("l", 8, 15))
print(s1.index("Python"))
# print(s1.index("Jaypal"))
print(s1.find("Jaypal"))
"""
s2 = "9428128473"
s3 = "Alakh9428128473"
s4 = "Alakh Pandya9428128473"
s5 = "AlakhPandya"
"""
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())
print(s5.isalpha())
# print(s1())       Not Callable error

s6 = "2021"
s7 = "½"
s8 = "5²"
s9 = "二千〇二十一"
print(s6.isnumeric())
print(s6.isdigit())
print(s6.isdecimal())

print(s7.isnumeric())
print(s7.isdigit())
print(s7.isdecimal())

print(s8.isnumeric())   # considers 0-9,subscript,superscript,circled numbers, vulgar fractions, digits from other languages etc
print(s8.isdigit())     # considers 0 to 9, superscript, subscripts & circled numbers
print(s8.isdecimal())   # considers strictly 0 to 9 only

print(s9.isnumeric())
print(s9.isdigit())
"""
s10 = "for"
s11 = "ifforinwhile"
print(s1.isidentifier())
print(s10.isidentifier())
print(s11.isidentifier())