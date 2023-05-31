# Modules & Packages
# Organizing our code in Modules & Packages
"""
import recursive_functions

print("8!=", recursive_functions.fact(8))
"""
# Giving an alias to the module
"""
import recursive_functions as rf

print("8!=", rf.fact(8))
"""
# Common examples:
"""
import speech_recognition as sr
import numpy as np
import pandas as pd
"""
# Don't create a function with the same name as a module
"""
import recursive_functions

def recursive_functions():
    print("I am recursive")

print("8!=", recursive_functions.fact(8))
recursive_functions()
"""
# importing specific functions from the module
"""
from recursive_functions import fact, geometric_progression as gp, arithmetic_progression as ap

print("8!=",fact(8))
print(gp(2, 3, 5))
print(ap(3, 5, 10))
"""
# importing all the functions from a module
"""
from recursive_functions import *

print("9!=", fact(9))
"""
import recursive_functions as rf
# from recursive_functions import fact

number = int(input("Enter the number to find its factorial: "))
print(f"{number}! = {rf.fact(number)}")
# print(f"{number}! = {fact(number)}")
print("importing program:", __name__)