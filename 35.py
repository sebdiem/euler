def is_prime(n):
    if n == 0 or n == 1: return False
    if n in (2,3,5,7): return True
    if not n%2: return False
    i = 3
    while i < int(n**0.5) + 1:
        if not n%i: return False
        i += 2
    return True

def is_circular(n):
        l = [int(c) for c in str(n)]
        m = len(l)
        for k in range(m):
            circular_perm = sum([l[i-k]*10**(m-1-i) for i in range(m)])
            if not is_prime(circular_perm): return False
        return True
print 7*13
print is_prime(17)

primes = [i for i in range(10**6+1) if is_prime(i)]
circular = [i for i in primes if is_circular(i)]
print circular, len(circular)
