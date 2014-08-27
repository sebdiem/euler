import math

def nearest_power_of_10(n):
    k = 0
    while 10**k < n:
        k += 1
    return 10**(k-1)

def decompose(n):
    if n < 10: return [n]
    result = []
    k = nearest_power_of_10(n)
    l = int(n/k)
    result = [l] + decompose(n-l*k)
    return result

    
print sum(decompose(math.factorial(100)))