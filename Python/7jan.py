"""
stock = []
class Car:
    wheels = 5          # class variable
    seating_capacity = 5
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel
    
    @classmethod
    def addNewCar(cls):
        print("Enter the following details of new car:")
        name = input("Name: ")
        price = int(input("Price: "))
        fuel = input("Fuel Type: ")
        return cls(name, price, fuel)
    def printDetails(self):
        print(f"Details of {self.name}".center(50, "-"))
        print("Name:", self.name)
        print("Price:", self.price)
        print("Fuel Type:", self.fuel)
        print("Wheels:", self.wheels)
        print("Seating Capacity:", self.seating_capacity)
        print("-".center(50, "-"))


while True:
    print("Press 1 to add new car")
    print("Press 2 to print details of an existing car")
    print("Press 3 to change details of a car")
    print("Press 4 to delete a car")
    print("Press 9 to exit")
    choice = int(input())
    if choice == 1:
        stock.append(Car.addNewCar())
    elif choice == 2:
        print("Sr.No.\tName of the Car")
        for car in stock:
            print(f"{stock.index(car)}\t\t{car.name}") 
        c = int(input("Which car's details do you want to see? Enter sr.no: "))
        stock[c].printDetails()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 9:
        break
    else:
        print("Invalid input, please try again...")
"""
# 4 pillars of OOP: Inheritance, Polymorphism, Abstraction, Encapsulation
"""
Types of inheritance:
Single/Simple inheritance:
    parent class-->child class

Multilevel Inheritance:
    Parent Class --> Child Class --> Grand Child Class

Hierarchical Inheritance:
                    --> Child Class 1
    Parent Class    --> Child Class 2
                    --> Child Class 3

Multiple Inheritance:
    Parent Class 1
    Parent Class 2  --> Child Class
    Parent Class 3

Hybrid Inheritance:
    Parent Class --> Child Class 1
                 --> Child Class 2 --> Grand Child Class
"""
# Employee Management System
class Employees():
    no_of_leaves = 8
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self.age = age

    def printDetails(self):
        print(f"Details of {self.name}".center(50, "-"))
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Leaves per month: ", self.no_of_leaves)
        

class Managers(Employees):
    team_size = 10
    education = "MBA"
    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience

    def printDetails(self):
        super().printDetails()
        print("Team Size: ", self.team_size)
        print("Education: ", self.education)
        print("-".center(50, "-"))

class Peons(Employees):
    no_of_leaves = 4

    def printDetails(self):
        super().printDetails()
        print("-".center(50, "-"))

class SalesExecutives(Employees):
    pass

class Accountants(Employees):
    pass

class GeneralManagers(Managers):
    experience = 10
    team_size = 150
"""
m1 = Managers()
print(m1.no_of_leaves)
p1 = Peons()
print(p1.__dict__)
print(p1.no_of_leaves)
# print(m1.education)
# MRO: Method Resolution Order
"""
m1 = Managers("Sunidhi", 30, "Female", 5)
p1 = Peons("Ramesh", 18, "Male")
m1.printDetails()
p1.printDetails()

# Next lecture: class method in parent class, multiple inheritance