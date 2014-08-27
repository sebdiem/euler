import math
def number_of_dividers(n):
    if n == 0: return 0
    if n == 1: return 1
    result = 0
    i = 1
    while i < (n+1)/2 + 1: 
        if not n%i:
            result += 1
        i += 1
    return result + 1

def test(i):
    if i%2:
        di = number_of_dividers(i)
        di_plus_one = number_of_dividers((i+1)/2)
    else:
        di = number_of_dividers(i/2)
        di_plus_one = number_of_dividers(i+1)
    return di*di_plus_one

def triangle(n):
    i = 8
    while test(i) <= n:
        i += 1
    return i

print number_of_dividers(11*12/2)
print test(11)
N = triangle(500)
print N*(N+1)/2