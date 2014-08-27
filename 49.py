
import itertools

memo = {}
def is_prime(n):
    if n == 1 or n == 0: return False
    if n == 2 or n == 3: return True
    if memo.has_key(n): return memo[n]
    i = 2
    while i <= n**0.5:
        if not n%i:
            memo[n] = False
            return False
        i += 1
    memo[n] = True
    return True

primes = [i for i in range(10**3, 10**4) if is_prime(i)]
i=0
while i < len(primes):
    p = primes[i]
    count = [p]
    for perm in itertools.permutations(str(p), 4):
        p2 = int("".join(perm))
        if p2 != p and p2 > 1000:
            if is_prime(p2):
                if p2 in primes: primes.remove(p2)
                if not p2 in count: count.append(p2)
    count.sort()
    diff = [(c1,c2,c3) for c1 in count for c2 in count for c3 in count if c3 > c2 > c1 and c3 - c2 == c2 - c1]
    if diff:
        print diff, "".join(map(lambda x: "".join(map(lambda y: str(y), x)), diff))
    i += 1
   
   
   

