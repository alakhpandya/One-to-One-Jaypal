# Passing collections as arguments to a function:
"""
def avg(n):
    return sum(n)/len(n)

l1 = [3, 4, 5, 6, 7, 8, 9]
print(f"avg of list = {avg(l1)}")
t1 = (5,6,7,8,9,10)
print(f"avg of tuple = {avg(t1)}")
s1 = {1,2,3,4}
print(f"avg of set = {avg(s1)}")
d1 = {1:"Mitesh", 2: "Riya", 3:"Roy"}
print(f"avg of dictionary = {avg(d1)}")
"""
# Args & Kwargs : Taking variable length arguments
"""
def average(*args):
    print(args)
    print(type(args))
    return sum(args)/len(args)
"""
"""
def average(n, *args):  # we may have any number of positional arguments but all of them must come before *args
    print(args)
    print(type(args))
    return (sum(args)+n)/(len(args)+1)

def average2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs.values())/len(kwargs)

average(5, 15, 34, 5)
print(f"Average of marks = {average2(Physics=47, Chemistry=48, Maths=50, Biology=44)}")
# average2(1="Mihir", 2="Ronit")    can't use kwargs like this
average(3)
"""
def func1(n1, n2, n3, *args, **kwargs):
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"n3 = {n3}")
    print(args)
    print(kwargs)

func1(11,12,13,141,513,22,490, Phy=50, math=49)

"""
Rule:
1st comes all the positional arguments
2nd comes *args (can be left empty)
3rd comes *kwargs (can be left empty)
"""
# HW:
"""
Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""