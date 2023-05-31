# Dictionaries: Unordered & Mutable collections of key:value pairs.
d1 = {101 : "Jaypal", 201 : "Akhilesh", 103 : "Maitri"}
# print(d1[0])   #   Dictionaries are unordered
d2 = {201 : "Akhilesh", 101 : "Jaypal", 103 : "Maitri"}
print(d1 == d2)
d3 = {"Jaypal" : "Python", "Aniruddh" : "Maths", "Shreya" : "Physics", "101" : "Alakh"}
print(d1[201])

d1[201] = "Rishabh"
print(d1)
print(len(d3))
print(min(d3))
print(max(d3))
print(sorted(d3))

d4 = {"Jaypal": "Gujarati", "Rahul": 5,"Madhusudan Sir": ["Soup", "Main Course", "Ice cream"], "Dhiraj Sir": ("Khichdi", "Kadi", "Buttermilk"), "Alakh": {"Kadi", "Khichdi", "Thumbsup"}, "Krishna Mam": frozenset({"Soup", "Punjabi", "Thumbsup"}), "Tejas Sir" : {"BF":"Maggie", "Lunch":"Punjabi", "Dinner":"Gujarati"}}
print(d4)
person = input("Whose meal do you want to see?")
if person == "Tejas Sir":
    meal = input("Which meal do you want to see? BF, Lunch or Dinner? ")
    print(d4[person][meal])

elif person == "Jaypal" or person == "Rahul":
    print(d4[person])

else:
    for x in d4[person]:
        print(x)
