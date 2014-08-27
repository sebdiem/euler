memo = {}
def next(n):
    if memo.has_key(n): return memo[n]
    if n == 89: return True
    if n == 1: return False
    next_n = sum([int(c)**2 for c in str(n)])
    memo[n] = next(next_n)
    return memo[n]


print next(145)
print next(42)
print next(20)
print next(4)
print next(16)
print next(37)
print next(58)
print next(44)
print next(32)
print next(13)
print next(10)
print next(10**7)
print next(2)

"""
N = 10**7
i = 1
while i <= N:
    next(i)
    i+= 1
print len(filter(lambda x: x[1], memo.items())) + 1 # +1 for 89"""
