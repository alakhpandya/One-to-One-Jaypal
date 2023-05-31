"""
class Employees():
    no_of_leaves = 8
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printDetails(self):
        print(f"Details of {self.name}".center(50, "-"))
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Leaves per month: ", self.no_of_leaves)

    @staticmethod
    def addEmployee():
        print("----------Enter the following details---------")
        name = input("Name: ")      # Om
        age = int(input("Age: "))   # 21
        gender = input("Gender: ")  # male
        return (name, age, gender)

class Managers(Employees):
    team_size = 10
    education = "MBA"
    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience

    def printDetails(self):
        super().printDetails()
        print("Experience: ", self.experience)
        print("Team Size: ", self.team_size)
        print("Education: ", self.education)
        print("-".center(50, "-"))

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        experience = int(input("Experience: "))
        return cls(name, age, gender, experience)

class Peons(Employees):
    no_of_leaves = 4

    def printDetails(self):
        super().printDetails()
        print("-".center(50, "-"))

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

class SalesExecutives(Employees):
    pass

class Accountants(Employees):
    pass

class GeneralManagers(Managers):
    experience = 10
    team_size = 150
    
"""
# Multiple Inheritance and Diamond problem
"""
class Father():
    hobby = "Cricket"
    education = "Doctor"

class Mother():
    education = "MBA"
    hobby = "Chess"

class Son(Father, Mother):
    education = "Grade 12"

class Daughter_in_law(Mother, Father):
    education = "First Year College"

class Grand_child(Son, Daughter_in_law):
    education = "sr.kg"

s = Son()
print(s.education)
print(s.hobby)
d = Daughter_in_law()
print(d.education)
print(d.hobby)
gc = Grand_child()
print(gc.hobby)
"""
# Abstraction: 
"""
1. We want to restrict creation of objects in a particular class.
2. We want to make some methods compulsary for all child classes to have.
"""
from abc import ABC, abstractmethod     # abstract base classes
                                        # ABC : abstract base class

class Employees(ABC):
    no_of_leaves = 8
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def printDetails(self):
        print(f"Details of {self.name}".center(50, "-"))
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Leaves per month: ", self.no_of_leaves)

    @staticmethod
    @abstractmethod
    def addEmployee():
        print("----------Enter the following details---------")
        name = input("Name: ")      # Om
        age = int(input("Age: "))   # 21
        gender = input("Gender: ")  # male
        return (name, age, gender)

class Managers(Employees):
    team_size = 10
    education = "MBA"
    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience

    def printDetails(self):
        super().printDetails()
        print("Experience: ", self.experience)
        print("Team Size: ", self.team_size)
        print("Education: ", self.education)
        print("-".center(50, "-"))

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        experience = int(input("Experience: "))
        return cls(name, age, gender, experience)

class Peons(Employees):
    no_of_leaves = 4

    def printDetails(self):
        super().printDetails()
        print("-".center(50, "-"))

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

class SalesExecutives(Employees):
    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

    def printDetails(self):
        super().printDetails()

class Accountants(Employees):
    pass

class GeneralManagers(Managers):
    # experience = 10
    team_size = 150

# e1 = Employees("Mantra", 19, "Male")
# e1.printDetails()
# g1 = GeneralManagers("Heli", 27, "Female", 5)
# g1.printDetails()
s1 = SalesExecutives("Prayag", 24, "Male")

# Next lecture: Encapsulation