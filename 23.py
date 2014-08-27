def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if not n%i: return False
    return True

N = 28123
primes = [i for i in range(2,N+1) if is_prime(i)]

def dividers(n):
    if n == 1: return [1]
    for p in primes:
        if not n%p:
            div = dividers(n/p)
            return div + [p*d for d in div if p*d not in div]

memo = {}
def is_abundant(n):
    if n == 0 or n == 1: return False
    if memo.has_key(n): return memo[n]
    memo[n] = sum(dividers(n)[:-1]) > n
    return memo[n]


total = 0
print "start"
result = []
for i in range(1, N+1):
    sab = False
    print i
    for j in range(1, i):
        if is_abundant(i-j) and is_abundant(j):
            sab = True
            break
    if not sab:
        result.append(i)
print sum(result)
