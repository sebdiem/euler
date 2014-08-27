def is_prime(n):
    if n == 0 or n == 1: return False
    if n in (2,3,5,7): return True
    if not n%2: return False
    i = 3
    while i < int(n**0.5) + 1:
        if not n%i: return False
        i += 2
    return True

N = 10**6
primes = [i for i in range(2,N+1) if is_prime(i)]
i = 9
while i < N:
    if not is_prime(i):
        j = 1
        goldbach = False
        while primes[j] < i:
            k = ((i-primes[j])/2)**0.5
            if k == int(k): 
                goldbach = True
                break
            j += 1
        if not goldbach: break
        print i, primes[j], k
    i += 2
print i
