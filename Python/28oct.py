"""
Make a Python recursive function that calculates & prints nth term of an arithmetic progression whose first term is 'a' and common difference is 'd' where, a, d & n are given by the user.
a = 6
d = 5
ap: 6, 11, 16, 21, 26, 31, 36, 41, 46,.....
n = 9
Traditional Approach:
nth term = a + (n-1)d = 6 + (8)5 = 46   
Recursive Approach:
9th term = 8th term + d
8th term = 7th term + d

1st term = a
nth term = (n-1)th term + d
"""
def recNat(start, n):
    if start == n+1:
        return n+1
    else:
        print(start, end="\t")
        return recNat(start+1, n)

n = int(input("Enter the number: "))
recNat(1, n)