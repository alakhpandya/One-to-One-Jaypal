# Some misc topics regarding functions
# Docstring
'''
import random

def avg(n1, n2, n3):
    """returns average of 3 numbers"""
    ans = n1 + n2 + n3
    """You can not use 4 variables"""
    return ans/3

print(avg.__doc__)
print(random.choices.__doc__)
'''
# Copying & deleting a function
# Rule of Thumb: We put () after a function only when (1) we want to define it (2) we want to call it. Nowhere else.
'''
def func1():
    print("I am func 1")

func2 = func1
func2()
del func1
# func1()
func2()

l1 = [1,2,3,4]
l2 = l1
l1.append(5)
del l1
print(l2)
'''
# Function calling another function
'''
def avg_of_factorials(n1, n2, n3, n4, n5):
    return (fact(n1)+fact(n2)+fact(n3)+fact(n4)+fact(n5))/5

def fact(n):
    f = 1
    for x in range(1, n+1):
        f *= x
    return f

print("Enter 5 integers: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(avg_of_factorials(a, b, c, d, e))
'''
# Lambda Function (Anonymous functions/ inline functions)
"""
def avg(n):
    return sum(n)/len(n)
"""
# l1 = [1,2,3,4,5,6]
# avg = lambda n : sum(n)/len(n)
# print(avg(l1))
def fact(n):
    f = 1
    for x in range(1, n+1):
        f *= x
    return f

avg_of_factorials = lambda n1, n2, n3, n4, n5 : (fact(n1)+fact(n2)+fact(n3)+fact(n4)+fact(n5))/5
print("Enter 5 integers: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(avg_of_factorials(a, b, c, d, e))

# function returning some condition, function returning a built in function, Passing function as an argument, Scope of a variable, local & global variables & global keyword & Nesting of functions