"""
d1 = {101 : "Jaypal", 201 : "Akhilesh", 103 : "Maitri", 201 : "Bhavya"}
# Keys must be unique & immutable.
# d1.clear()
# del d1
# del d1[201]
# print(d1)
d2 = d1.copy()
bpp = ["a", "b", "c", "d"]
d3 = dict.fromkeys(bpp, 500)
print(d3)
print(d1[103])
print(d1.get(103))
# print(d1[105])
print(d1.get(105, "Not Existing"))
print(d1.keys())
print(d1.values())
print(d1.items())
# print(d1.pop(103))
# print(d1)
# print(d1.popitem())
# print(d1)

d1.update(d3)
print(d1)
"""
d4 = {"Alakh":"Salad", "Dhiraj":"Dal-Rice", "Jaypal":"Paubhaji", "Hetal":"Panipuri"}
key = input("Enter new key: ")
value1 = input("Enter its value: ")
value2 = d4.setdefault(key, value1)
if value1 != value2:
    print(f"Key: {key} is already present with value: {value2}")
    overwrite = input("Do you want to overwrite? y or n?")
    if overwrite == 'y':
        d4[key] = value1
    else:
        print("Key-value pair could not be added...")
print(d4)