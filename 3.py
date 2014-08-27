import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if not n%i:
            return False
    return True

def euclide(n):
    max_divider = 0
    for i in range(1,int(math.sqrt(n))+1):
        if not n%i and is_prime(i):
            max_divider = i
    return max_divider

print euclide(600851475143)
