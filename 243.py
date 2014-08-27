from fractions import gcd
import time

def is_prime(n):
    if n == 1 or n == 0: return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i: return False
    return True

N = 10**5
primes = [i for i in range(2, N) if is_prime(i)]

memo = {}
def decompose(n):
    if memo.has_key(n): return memo[n]
    for i in primes:
        if i == n or i > n:
            memo[n] = {n:1}
            return {n:1}
        if not n%i:
            d = decompose(n/i)
            if d.has_key(i): d[i] += 1
            else: d[i] = 1
            memo[n] = d
            return d

print decompose(6)

def sigma(n):
    d = decompose(n).keys()
    print d
    used = []
    result = 0
    for i in d:
        for k in range(1, n/i):
            if not k*i in used:
                result += 1
                used.append(k*i)
    return result

def sigma2(n):
    result = 0
    for i in xrange(2, n):
        if gcd(i,n) > 1: result += 1
    return result


   
def R(n):
    return n-1-sigma2(n)
   
def problem243():
    i = 223092870
    while i < 6469693230:
        d = decompose(i)
        s = spec_sigma(d)
        print i, s/(i-1.)
        if s*94744 < (i-1)*15499: return i
        i+=1
  
def spec_sigma(d):
    if len(d) <= 1: return 1
    keys = d.keys()
    v = d.items()
    p = lambda x,y: x*y
    d = dict([(k,1) for k in keys if k != keys[-1]])
    return (keys[-1]-1)*spec_sigma(d)*reduce(p,[i**(k-1) for i,k in v])

#print problem243()
#N = reduce(lambda x,y:x*y, primes[:9])
#N = reduce(lambda x,y:x*y, primes[:9])
"""N = 223092870
print N
d = decompose(N)
start = time.time()
r = spec_sigma(d)
end = time.time()
print "time1:", end-start
r2 = N-1-sigma2(N)
print "time2:", time.time()-end
print N,r,r/(N-1.)
print N,r2,r2/(N-1.)

print problem243()"""


def count_primes_to(d):
    if len(d) == 1 and d[d.keys()[0]] == 1: return d.keys()[0] - 1
    keys = d.keys()
    keys.sort()
    v = d.items()
    product = lambda x,y: x*y
    v = [i**(k-1) for i,k in v]
    M = reduce(product, v)
    if M == 1:
        d = dict([(k,1) for k in keys if k != keys[-1]])
        return (keys[-1]-1)*spec_sigma(d)
    else:
        d = dict([(k,1) for k in keys])
        return M*spec_sigma(d)

d1 = [decompose(i) for i in range(20)]
d = decompose(20)
print d
print count_primes_to(d)
"""
for i in range(1,100):
    d = decompose(i)
    c = count_primes_to(d)
    r2 = i-1-sigma2(i)
    if c != r2:
        print i,c,r2"""

