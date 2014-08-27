import math

def is_prime(n):
    if n == 0 or n == 1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if not n%i: return False
    return True

def collect_primes(n):
    result = []
    for i in range(n+1):
        if is_prime(i): result.append(i)
    return result

def sum_consecutive_primes(primes, limit):
    best = 1
    best_prime = 2
    for i in range(len(primes)-1):
        if (len(primes)-i) < best or best*primes[i] + best*(best-1) > limit:
            return best, best_prime
        curr = primes[i]
        for j in range(i+1, len(primes)):
            curr += primes[j]
            if curr > limit: break
            if is_prime(curr) and j-i+1 > best:
                best = j-i+1
                best_prime = curr
                print "best: ", i, j, best, best_prime
    return best, best_prime

c = collect_primes(1000000)
print "primes collected"
print sum_consecutive_primes(c, 1000000)
