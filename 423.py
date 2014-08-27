import math
import bisect
fact = math.factorial

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

N = 50*10**6
primes = primes_sieve2(50*10**6+100)
primes = zip(primes[:-1], primes[1:])
print primes[-1]
print "finished with primes"

def pi(n):
    return bisect.bisect_right(primes, n)

def eucl(r1, u1, v1, r2, u2, v2):
    if r2 == 0: return (r1, u1, v1)
    q = r1/r2
    return eucl(r2, u2, v2, r1 - q*r2, u1 - q*u2, v1 - q*v2)

def euclid(a, b):
    return eucl(a, 1, 0, b, 0, 1)   
 
def invert(a, b, n):
    # gives a solution x to ax = b in Z/nZ
    return b*euclid(a, n)[1]

def Comb(k, n):
    if k == 0: return 1
    return (Comb(k-1, n-1)*n)/k


# formule trouvee par observation sur les dix premiers resultats
# card{c=i pour n elements} = Comb(n-1-i, n-1)*(6*5**(n-i-1))
c = lambda n, i: Comb(n-1-i, n-1)*(6*5**(n-i-1))

def S(N):
    previous = 6
    result = 6
    i = 0
    sav = 0
    cminus1 = 6
    k = 0
    for p1,p2 in primes:
        if p1 > N: break
        n = p1
        p = i + 1
        temp = ((n-1)*cminus1)%1000000007
        temp = invert(p, temp, 1000000007)
        previous = (6*previous + temp - cminus1)%1000000007
        result += previous%1000000007
        #s = str(previous)
        cminus1 = temp
        n += 1
        while n < p2 and n <= N:
            previous = ((6*previous) - cminus1)%1000000007
            result += previous%1000000007
            #s += " %s" % str(previous)
            cminus1 = (5*(n-1)*cminus1)%1000000007
            cminus1 = invert((n-1-p), cminus1, 1000000007)
            n += 1
        i += 1
        #print s
        if math.log(p2) > k:
            print p2
            k += 1
    print "last primes: ", p1, p2
    return result

print S(N)%1000000007
