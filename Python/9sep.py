"""
Operators in Python
1.  Arithmetic Operators
        +
        -
        *
        /
        %
        //      floor division
        **      exponent/power

2.  Relational Operators/Comparision Operators
    These operators will always return either True or False
        <
        >
        <=
        >=
        ==
        !=

3.  Logical Operators
        and : and gives you True only if all the conditions involved are True
        or:   or gives you True if any of the conditions involved is True 
             (or gives False only when all the conditions involved are False.)
        not:  

4.  Bitwise Operators        
        and: &
            3 & 5
            3 : 0 0 1 1
            &   & & & &
            5 : 0 1 0 1
            -----------
                0 0 0 1 = 1
        
        or: |
            3 & 5
            3 : 0 0 1 1
            |   | | | |
            5 : 0 1 0 1
            -----------
                0 1 1 1 = 7

                Normal Or:
                If you have either degree in computers or 5 years experience then you are eligible for the job.
                    Person  Degree  Exp.    Eligible
                    Alakh   0       0       0
                    Subahu  0       1       1
                    Arjun   1       0       1
                    Jaypal  1       1       1

                Exclusive Or (xor): xor gives you True if odd number of inputs are True
                What would you like to have? Tea or Coffee?
                If you get above 90% I will gift you either Macbook air or iPhone.
                    Person  Degree  Exp.    Eligible
                            Air     iPhone  OK?
                    Arjun   0       0       0
                    Subahu  0       1       1
                    Jaypal  1       0       1
                    Alakh   1       1       0

        xor: ^
            3 ^ 5
            3 : 0 0 1 1
            ^
            5 : 0 1 0 1
            -----------
                0 1 1 0 = 6

        not: ~
            ~5
            5 : 0 1 0 1
            -----------
                1 0 1 0 = - 6

        Left shift : 5 << 3
            5 : 0 0 0 0  0 1 0 1
            <<: 0 0 0 0  1 0 1 0 = 10
            <<: 0 0 0 1  0 1 0 0 = 20
            <<: 0 0 1 0  1 0 0 0 = 40

        Right Shift : 120 >> 3
           120: 0 1 1 1  1 0 0 0
           >> : 0 0 1 1  1 1 0 0 = 60
           >> : 0 0 0 1  1 1 1 0 = 30
           >> : 0 0 0 0  1 1 1 1 = 15
           >> : 0 0 0 0  0 1 1 1 = 7

5.  Assignment Operators
        =   
            a = 9   : Hey computer, i want to store an integer 9. Give me some space. And remember, I will call that 'a'
            
            x = 5 * 3 + 7 / 2
             <--
            5 + 7 = x   Wrong
            x = 5 + 7   Right

        +=  a += b  :   a = a + b
        -=  a -= b  :   a = a - b
        *=  a *= b  :   a = a * b
        /=  a /= b  :   a = a / b
        %=  a %= b  :   a = a % b
        //=  a //= b:   a = a // b
        **=  a **= b:   a = a ** b
        &=  a &= b  :   a = a & b
        |=  a |= b  :   a = a | b
        ^=  a ^= b  :   a = a ^ b
        <<=  a <<= b:   a = a << b
        >>=  a >>= b:   a = a >> b

    = is used to swap values of two variables

6.  Identity Operators
        is
        is not

7.  Membership Operators
        in
        not in
"""
"""
x = 11
y = 4
print(x/y)
print(x//y)
print(x ** y)
print(x > y)
print(x <= y and x <= 15)
print(x <= y or x <= 15)
print(not x <= y)

print(3 & 5)
print(3 | 5)
print(3 ^ 5)
print(~5)
print(5 << 3)
print(120 >> 3)
print(120 >> 4)
x = 13
y = 24
x, y = y, x
print(f"x : {x}")
print(f"y : {y}")
"""
l1 = [2,4,6,8,10]
l2 = l1
l3 = l1.copy()
print(l1 is l2)
print(l1 is l3)
print(l1 == l3)
s1 = "Jaypal is a good boy!"
print("good" in s1)
print("best" in s1)