import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if not n%i: return False
    return True

N = 2000000
result = 2
for i in range(3, N+1, 2):
    if is_prime(i):
        result += i
print result
