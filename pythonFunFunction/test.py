import math

def fattRiccardo(n):
    if n == 1:
        return 1
    else:
        return n * fattRiccardo(n - 1)
print(fattRiccardo(1))

def fattNumberphile(n):
    return int(fattRiccardo(n + 1) / (n + 1))
print(fattNumberphile(1))

def divisionSub(a, b):
    c = a - b
    resto = 0
    i = 1
    while c > 0:
        if c - b >= 0:
            c -= b
            i += 1
        else:
            resto = c
            break
    return i + (resto / b))
print(divisionSub(125.1, 2))
