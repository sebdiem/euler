import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if not n%i: return False
    return True


total = 6
i = 15
while total < 10001:
    if is_prime(i):
        total += 1
        print total, i
    i += 2

print i-2
