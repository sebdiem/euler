def is_prime(n):
    if n == 0 or n == 1: return False
    if n == 2 or n == 3: return True
    i = 2
    while i <= n**0.5:
        if not n%i: return False
        i += 1
    return True

N = 10**5
primes = [i for i in range(N) if is_prime(i)]
print "ok primes"

memo = {}
def num_of_primes_sum(n):
    if n == 2: return set()
    if n == 3: return set()
    if memo.has_key(n): return memo[n]
    result = set()
    for p in primes:
        if p <= n/2:
            if is_prime(n-p):
                result.add((p, n-p))
            r = num_of_primes_sum(n-p)
            for t in r:
                result.add(tuple(sorted(t + (p,))))
    memo[n] = result    
    return result
            

for i in xrange(N):
    if len(num_of_primes_sum(i)) > 5000:
        print i
        break
