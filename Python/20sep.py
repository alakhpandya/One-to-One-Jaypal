"""
class work:
1. Make a Python program that takes a user defined list of countries from user, then ask user for a specific country and checks whether that country is in the list or not.
2. Make a Python program that checks whether the number given by user is prime or not.

countries = []
no = int(input("How many countries do you want in the list? "))
print(f"Enter {no} countries:")
while no > 0:
    country = input()
    countries.append(country)
    no -= 1
search = input("Enter the name of the country you want to search: ")
if search in countries:
    print(f"{search} is in the list")
else:
    print(f"{search} is not in the list")
"""
no = int(input("Enter The Number"))
if no > 1:
    for i in range(2,no):
        if no % i == 0:
            print(no, "is not a prime number")
            break
    else:
        print("not prime.")
else:
    print("not prime.")
"""
for else & while else:
    code inside else block will be executed only if the loop completes all the iterations and not broken by break statement. If break statement is executed, else block will not execute.
"""