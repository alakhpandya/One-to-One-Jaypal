fruits = ["kiwi", "mango", "banana", "cherry", "apple"]
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1
"""
for x in fruits:  # i = "kiwi", "mango", "banana", "cherry", "apple"
    print(x)

for fruit in fruits:
    if fruit == "cherry":
        # break
        # continue
        # pass
    print(fruit)
print("Thanks!")

s1 = "Python@Royal"
for character in s1:
    print(character)
"""
# for loop in range
# for(i = 0; i < 5; i++)
"""
for i in range(5):  # range(5) = 0,1,2,3,4
    print(i)


# for(i = 0; i <= n; i++)
for i in range(n+1)

for (i = 5; i < 15; i++)
for i in range(5, 15)

for (i = 5; i < 15; i= i + 2)
for i in range(5, 15, 2)


students_data = [
    ["Rahul", 20, "Electronics"],
    ["Parag", 19, "Chemistry"],
    ["Neha", 18, "Physics"],
    ["Gopi", 22, "IT"]
]
# for subList in students_data:
#     print(subList)
for x, y, z in students_data:
    print(f"{x} is {y} years old & studies {z}")
"""

# student_data = ["Rahul", ["West Begal", "Kolkata"], "Electronics"]
"""
name = student_data[0]
age = student_data[1]
major = student_data[2]
"""
# unpacking a collection
# name, region, major = student_data
# student_data = ["Parag", 19, "Chemistry", "Guitar", "Soldier", "Gandhinagar"]

"""
name, age, *others = student_data
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Other details: {others}")


*details, profession, city = student_data
print(f"Profession: {profession}")
print(f"City: {city}")
print(f"Other details: {details}")

name, *details, city = student_data
print(f"Name: {name}")
print(f"City: {city}")
print(f"Other details: {details}")
"""
student_data = ["Gopi", 22, "IT"]
# name, age = student_data
name, age, hobby, major = student_data

"""
Class work:
1. Make a program in Python to create a user defined list.

HW:
1. Ask an input from the user & print whether that input is present in the list or not.
2. Ask a number from user & check whether it is prime number or not.
"""
# Next Lecture: while else & for else