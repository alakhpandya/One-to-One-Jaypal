# User Defined Function: 
"""
Types of the functions:
1. Without Argument, without return
2. With Arguments, without return
3. Without Argument, with return
4. With Arguments, with return



"""
# import area
# global variables & constants area
# function area
# main program area
"""
def printPython():
    print("Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30] \nPython is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a \"batteries included\" language due to its comprehensive standard library.")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a > b:
    printPython()

# Make a Python program that prints factorial of a given number and it uses a function to find factorial of a number.
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"{n}! = {fact}")

a = int(input("Enter any integer: "))
factorial(a)
"""
# Make a Python program that prints sum of factorials of 3 given integers and it uses a function to find factorial of a number provided in argument.
"""
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    # print(f"{n}! = {fact}")
    return fact

def avg(a, b):
    return (a + b)/2

a = int(input("Enter any 3 integers: "))
b = int(input())
c = int(input())
sum = factorial(a) + factorial(b) + factorial(c)
print("sum =", sum)
"""
# Make a Python program that asks two integers from the user & prints all the prime numbers between those two integers. Use Function named "primeCheck" to check whether the number given in the argument is prime or not.
"""
6 is a perfect no.
Because factors of 6 except itself adds up to 6: 1 + 2 + 3 = 6
"""
# Make a Python program that asks two integers from the user & prints all the perfect numbers between those two integers. Use Function named "perfectCheck" to check whether the number given in the argument is a perfect number or not.

def factor(x):
    factors = []
    for i in range(1, x):
        if x % i == 0:
            factors.append(i)
    return factors

def perfectCheck(n):
    if sum(factor(n)) == n:
        return True
    return False

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
print(f"Perfect numbers between {lower} & {upper} are:")
for i in range(lower, upper+1):
    if perfectCheck(i):
        print(i)