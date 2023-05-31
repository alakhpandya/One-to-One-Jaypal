# Make a Python program that asks two integers from the user & prints all the armstrong numbers between those two integers. Use Function named "armCheck" to check whether the number given in the argument is an armstrong number or not.
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
# Recursive Function
"""
5! = 1 x 2 x 3 x 4 x 5
5! = 5 x 4! = 5 x 24 = 120
4! = 4 x 3! = 4 x 6 = 24
3! = 3 x 2! = 3 x 2 = 6
2! = 2 x 1! = 2 x 1 = 2
1! = 1 x 0! = 1 x 1 = 1
0! = 1          <= Non Recursive step
n! = n * (n-1)! <= Recursive step
"""
"""
def func(n):
    if => Non Recursive step

    else => recursive step
"""
def recFact(n):
    if n == 0:
        return 1
    else:
        return n * recFact(n-1)

number = int(input("Enter any integer: "))
print(f"{number}! = {recFact(number)}")