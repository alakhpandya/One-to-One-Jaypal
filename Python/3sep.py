"""
s1 = "It's fun to learn Python."
s2 = "It's fun to learn Python.\n"
s1.islower()
s1.isupper()
s1.istitle()
print(s1.isprintable())
print(s2.isprintable())
s3 ="  \t\n  "
print(s3.isspace())
print(s1.split(" "))
s4 = "Jaypal,Patel,9925025261,jaypalp6604@gmail.com"
contact = s4.split(",")
print(s1.split(" ", 2))
print(s1.rsplit(" ", 2))
print(s2.split("\n"))
print(contact)
s5 = "_".join(contact)
print(s5)
print(s1.ljust(100, "."))
print(s1.rjust(100, "."))
s6 = "$$$$$Pyt$hon$$$$$$"
print(s6.lstrip("$"))
print(s6.lstrip("@"))
print(s6.rstrip("$"))
print(s6.strip("$"))

print(s1.partition("to"))
print(s1.partition("t"))
print(s1.rpartition("t"))

print(s1.replace("t", "th"))
print(s1.replace("t", "th", 2))

print(s1.rfind("t"))
print(s1.rfind("to"))
print(s1.rfind("too"))
print()
print(s1.rindex("t"))
print(s1.rindex("to"))
# print(s1.rindex("too"))
s7 = "I love my country.\nI also love Python.\nBecause it is very funny language."
print(s7.splitlines())
"""
dd = input("Date:")
mm = input("Month:")
print("Today's date in DD/MM/YYYY:", dd.zfill(2), "/", mm.zfill(2), "/ 2021")