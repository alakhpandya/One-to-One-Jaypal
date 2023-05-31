"""
from myPackage import important_functions as imp

print(imp.primeCheck(1003))
"""
"""
from myPackage.important_functions import perfectCheck as perfect

print(perfect(28))
"""
"""
from myPackage.subPackage import demo

demo.func1()
"""

from myPackage.subPackage.demo import func2 as f2

f2()

# Select atleast 2-3 built in modules of Python and create programs using atleast 2-3 functions of each of them.