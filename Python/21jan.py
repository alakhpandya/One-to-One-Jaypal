# Encapsulation
"""
class Employees():
    no_of_leaves = 8                                # public variable
    def __init__(self, name, age, gender):          # public method
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
    _salary = 50000                      # protected variable
    __admin = False                         # private variable

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

    def _updateSalary(self):                                # protected method
        self._salary = int(input("Enter new salary: "))

    def __promoteToAdmin(self):                             # private method
        self._Managers__admin = True

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

m1 = Managers("a", 30, "f", 5)
print(m1._salary)
# m1._updateSalary()
# print(m1._salary)

# print(m1.__admin)     Can not access private variable directly
print(m1._Managers__admin)          # name mangling
m1._Managers__promoteToAdmin()
print(m1._Managers__admin)
"""
# Exception Handling
"""
while True:
    try:
        a = int(input("Enter Two numbers:\n"))
        b = int(input())
        break
    except ValueError:
        print("Only integers please... Try again")
try:
    print(a/b)
except ZeroDivisionError:
    print("Oops! it seems like you are trying to divide by 0! please try again...")
"""
"""
try:
    a = int(input("Enter Two numbers:\n"))
    b = int(input())
    print(a/b)

except ValueError:
    print("Only integers please... Try again")

except ZeroDivisionError:
    print("Oops! it seems like you are trying to divide by 0! please try again...")

finally:
    print("This will be executed always")
"""
"""
try:
    a = int(input("Enter Two numbers:\n"))
    b = int(input())
    print(a/b)

except:                                     # handle ALL THE EXCEPTION including keyboardInterrupt
    print("Something went wrong...")
"""
try:
    a = int(input("Enter Two numbers:\n"))
    b = int(input())
    print(a/b)

except Exception as e:      # handles all the exceiptions except keyboardInterrupt
    print(e)                # stores the message of exception in 'e'