# Object Oriented Programming
# DRY: Do not repeat yourself
# Easy to make difficult programs with OOP
"""
x = 5
print(type(x))
# x.upper()
y = "My String"
print(type(y))

class int:
    pass

class str:
    def upper():
        pass
"""
class Car:
    wheels = 5          # class variable
    seating_capacity = 5

c1 = Car()
c1.name = "Creta"       # Object Variable
c1.price = 1500000
c1.fuel = "Petrol"

print(c1.name)
print(c1.price)
print(c1.fuel)
print(c1.wheels)

c2 = Car()
c2.name = "XUV500"
c2.price = 2000000
c2.fuel = "Deisel"
c2.seating_capacity = 7     # Object Variable with the same name as Class Variable

print(c2.name)
print(c2.price)
print(c2.fuel)
print(c2.wheels)
print(c2.seating_capacity)
print()
print(c1.seating_capacity)
print("Object Variables of c1:", c1.__dict__)
print("Object Variables of c2:", c2.__dict__)

print(c1)