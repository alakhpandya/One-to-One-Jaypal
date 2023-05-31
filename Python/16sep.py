# Make a Python program that counts the number of digits in a given number.
"""
n = int(input("Enter any number: "))
digit = 0
temp = n
while temp > 0:
    temp //= 10
    digit += 1
print(f"{n} has {digit} digits.")
"""
# infinite while loop
"""
while True:
    n1 = int(input("ENTER NO.1 "))
    n2 = int(input("ENTER NO.2 "))

    print("1---ADD")
    print("2---SUBTRACT")
    print("3---MULTIPLY")
    print("4---DIVIDE")
    print("5---FLOOR DIVISION")
    print("6---REMAINDER")
    print("7---EXPONENT")
    print("8---EXIT")

    choice = int(input("ENTER YOUR CHOICE "))

    if choice == 1:
        print("ADDITION",n1+n2)
    elif choice == 2:
        print("SUBTRACTION",n1-n2)
    elif choice == 3:
        print("MULTIPLICATION",n1*n2)
    elif choice == 4:
        print("DIVISION",n1/n2)
    elif choice == 5:
        print("FLOOR DIVISION",n1//n2)
    elif choice == 6:
        print("REMAINDER",n1%n2)
    elif choice == 7:
        print("EXPONENET",n1**n2)
    elif choice == 8:
        break
    else:
        print("INVALID CHOICE")
print("Thanks for using our calculator!")
"""