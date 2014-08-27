import math
factorial = math.factorial

k, l = 0, 1
current = 0
rest = range(10)
result = []
while current != 10**6:
    k = 0
    while current + k*factorial(10-l) < 10**6:
        k += 1
    k -= 1
    current += k*factorial(10-l)
    l += 1
    result.append(rest[k])
    rest.remove(rest[k])
    print current, result
    

print result
#2783915460
