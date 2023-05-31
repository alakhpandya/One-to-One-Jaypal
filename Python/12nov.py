# function returning some condition, function returning a built in function, Passing function as an argument, Scope of a variable, local & global variables & global keyword & Nesting of functions
"""
def func1(n):
    return n < 5

l1 = [1,2,3,4,5,6,7,8,9,10]
for x in l1:
    if func1(x):
        print(x)
    else:
        print(20-x)

def secret():
    return sum

def topSecret():
    return print

l1 = [1,2,3,4,5,6,7,8,9,10]
topSecret()((secret()(l1)))


def avg(n1, n2, n3, n4, n5):
    return (n1+n2+n3+n4+n5)/5

def fact(n):
    fa = n
    for x in range(1,n):
        fa *= x
    return fa

print("Enter 5 integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print("final answer =", avg(fact(a), fact(b), fact(c), fact(d), fact(e)))
"""
var3 = 30           # global variable
var4 = 40
def func1():
    var1 = 10       # local variable of func1
    func2()
    var3 = 100
    print(var1)
    print(var2)
    var3 += 1       # you can access global variable but can not change it.
    print(var3)
    # def func3():
    #     global var1       Can not change var1 even this way
    #     var1 += 1         can not change var1
    #     print(var1)       can just access var1

    # func3()
    global var4
    var4 += 1
    print(var4)

def func2():
    # var1 += 1
    # print(var1)
    print(var3)

# print(var1)
# func1()
var2 = 20           # global variable for all the fuctions called after this point
func1()
print(var3)
print(var4)