stock = []
class Car:
    wheels = 5          # class variable
    seating_capacity = 5
    
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel
    """
    def __init__(self):
        self.name
        self.price
        self.fuel
    """
    @classmethod
    def addNewCar(cls):
        print("Enter the following details of new car:")
        name = input("Name: ")
        price = int(input("Price: "))
        fuel = input("Fuel Type: ")
        return cls(name, price, fuel)

    def printDetails(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Fuel Type:", self.fuel)
        print("Wheels:", self.wheels)
        print("Seating Capacity:", self.seating_capacity)

class SellsExecutive():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def emi_calculator(price, interestRate, tenure):
        interestAmount = (price * interestRate * tenure) / 100
        total = price + interestAmount
        emi = total/(tenure*12)
        return emi

"""
c1 = Car("Creta", 1500000, "Petrol")

# c1.name = "Creta"       # Object Variable
# c1.price = 1500000
# c1.fuel = "Petrol"

c1.printDetails()

c2 = Car("XUV500", 2000000, "Deisel")

# c2.name = "XUV500"
# c2.price = 2000000
# c2.fuel = "Deisel"
# c2.seating_capacity = 7

c2.printDetails()
s1 = SellsExecutive("Roshan", 31, "Male")
print(s1.emi_calculator(1000, 5, 2))
"""
# c1 = Car("Alto", 400000, "CNG")
stock.append(Car("Alto", 400000, "CNG"))
print("Press 1 to add new car")
print("Press 2 to print details of an existing car")
print("Press 3 to add new employee")
print("Press 4 to calculate emi of a car")
choice = int(input())
if choice == 1:
    stock.append(Car.addNewCar())
elif choice == 2:
    c = int(input("Which car's details do you want to see? Enter sr.no: "))
    stock[c].printDetails()
elif choice == 3:
    pass
elif choice == 4:
    pass
elif choice == 9:
    pass
else:
    pass