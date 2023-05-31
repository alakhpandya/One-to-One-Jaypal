'''
c:
#include<stdio.h>
#include<conio.h>
void main()
{
	clrscr();
	printf("Hello World!");
	getch();
}
'''
"""
java:
class Main{
	public static void main(String args[])
	{
		System.out.println("Hello World!");
	}
}

# python:
print("Hello World!")
print("The location of Python interpreter is C:\\new folder\\temp\\Python")

Escape Sequence Characters in Python:
\
\n	new line
\t	tab
\b	back space
\r	carriage return

print("Jaypal\b\b\b Patel") # Jay Patel
print("Python\b\b\b\bPi")	# PyPion
print("Python is fun\r@Royal")
print("Welcome to the world of Python!", end="\n")
print("Ahmedabad")
print("Welcome to the world of Python!", end="")
print("Ahmedabad")
print("Welcome to the world of Python!", end="\t\tCity = ")
print("Ahmedabad")

# Variables in Python
a = 5
print(type(a))
b = 294387098100123948717132598710934701973094837059817010123982437019347328473920487329570169748519
print(type(b))
c= 12.89
print(type(c))
d =98234987234098254398301987509734289.93487198709243875097410
print(type(d))
e = 5j
f = 19 - 5j
print(type(e))
print(type(f))

str1 = "a"
str2 = "Jaypal is a good boy"
print(type(str1))
print(type(str2))

print("a")
print(a)
print("c =", c)	# c = 12.89
"""
# Taking inputs in Python
"""
print("Enter a number: ")
p = input()
print("Your number is :", p)
q = input("Enter second number: ")
print("Second number is :", q)
print("Enter two numbers:")
r = input()
s = input()
print("sum =", int(r) + float(s))
print("Enter two numbers:")
t = int(input())
u = float(input())
print("sum =", t + u)
v = str(t)
print(v, type(v))

print("Enter two Strings:")
s1 = input()
s2 = input()
s3 = (s1 + s2)*5
print(s3)
"""
print("Enter two numbers:")
t = int(input())	# t = 12
u = int(input())	# u = 4
print(t, "+", u, "=", t+u)	# 12 + 4 = 16
print(t, "-", u, "=", t-u)
print(t, "*", u, "=", t*u)
print(t, "/", u, "=", t/u)

"""
Expected Execution of program:

Enter 5 numbers:
2
3
4
5
6
Average of 2, 3, 4, 5, 6 is : 4.0
"""
# f-string
print("Enter 5 numbers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(f"Average of {a}, {b}, {c}, {d}, {e} is : {(a+b+c+d+e)/5}")