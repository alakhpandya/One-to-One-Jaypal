def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def arithmetic_progression(a, d, n):
    if n == 1:
        return a
    else:
        return d + arithmetic_progression(a, d, n-1)

def geometric_progression(a, r, n):
    if n == 1:
        return a
    else:
        return r * geometric_progression(a, r, n-1)

if __name__ == "__main__":
    print(fact(9))
    print(arithmetic_progression(4, 13, 15))
    print(geometric_progression(3, 4, 9))
print("module:", __name__)