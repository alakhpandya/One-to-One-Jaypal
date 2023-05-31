def average(n1, *args):
    return (sum(args)+n1)/(len(args)+1)

def primeCheck(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    else:
        return True

def perfectCheck(n):
    l1 = []
    for x in range(1, n):
        if n%x == 0:
            l1.append(x)
    if sum(l1) == n:
        return True
    else:
        return False