# Decision Making (if conditions)
# Python is indent-sensitive language
# Check whether the number given by user is positive or negative
"""
n = float(input("Enter any number: "))
if n > 0:
    print(f"{n} is a positive number.")

elif n == 0:
    print(f"{n} is neither positive nor negative number.")

else:
    print(f"{n} is a negative number.")

print("Thanks for using our program!")


n = float(input("Enter any number: "))
if n >= 0:
    print(f"{n} is a positive number.")

if n == 0:
    print(f"{n} is neither positive nor negative number.")

if n <= 0:
# else:
    print(f"{n} is a negative number.")

print("Thanks for using our program!")
"""
# Shorthand notations : Only for one-liner if statements
"""
n = float(input("Enter any number: "))
if n > 0: print(f"{n} is a positive number.")
"""
n = float(input("Enter any number: "))
print(f"{n} is a positive number.") if n > 0 else print(f"{n} is a negative number.")

# There is no shorthand for statements involving elif
# There is no switch case in Python so we use if, elif, else for the same

"""
Practice Programs:
1. Make a program to grade a student based on his marks input by user.
2. Make a menu-driven calculator to perform one of the operations from +, -, *, /, floor division, remainder & power based on the choice of user. 
"""