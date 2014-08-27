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

N = 10**6
primes = primes_sieve2(N+100)
print "finished primes"

def s(n,m):
    i = 0
    p = primes[i]
    result = 0
    while p <= m:
        if ((n%p)**15)%p == p-1:
            result += p
        i += 1
        p = primes[i]
    return result

print s(2, 10)
print s(2, 1000)
print s(10, 100)
print s(10, 1000)

result = 0
i = 0
p = primes[i]
while p <= N:
    for n in xrange(1, p):
        pass
        """
        if ((n%p)**15)%p == p-1:
            result += 10**11 - n
            break"""
    i += 1
    #print p, n
    p = primes[i]
print result
