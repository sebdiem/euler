import itertools

def is_prime(n):
    if n == 0 or n == 1: return False
    if n == 2: return True
    if n == 3: return True
    i = 2
    while i <= n**0.5:
        if not n%i: return False
        i += 1
    return True

N = 10**6
PRIMES = [p for p in xrange(N) if is_prime(p)]
print "Primes generated"

def repeating_digits(n):
    # do not allow the repeating digit in end position
    s = str(n)
    return set([c for c in s if s.count(c) == 3 and s[-1] != c])

def problem51(n=8, c=0):
    for p in PRIMES:
        for d in repeating_digits(p):
            if not c or str(p).count(d) == c:
                count = 0
                for i in range(10):
                    q = int(str(p).replace(d, str(i)))
                    if len(str(q)) == len(str(p)) and q in PRIMES:
                        count += 1
                if count == n:
                    return p

print problem51()
    
    
