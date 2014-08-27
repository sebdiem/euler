from bisect import bisect_left

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            n = i**2
            while n < limit:    # Mark factors non-prime
                a[n] = False
                n += i
    return map(lambda y: y[0], filter(lambda x: x[1], enumerate(a)))

N = 10**8
PRIMES = primes_sieve2(N/2)
result = 0
for i,p in enumerate(PRIMES):
    b = bisect_left(PRIMES, N/p)
    b = b if b == len(PRIMES) or PRIMES[b]*p >= N else b+1
    result += max(b-i, 0)

print result
