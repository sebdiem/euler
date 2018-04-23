import pickle
from collections import Counter
from collections import defaultdict
from itertools import combinations
from functools import reduce


global PRIMES
global PRIMES_SET


def build_primes(N=10**7):
    primes = [1] * N
    primes[0] = 0
    primes[1] = 0
    for i in range(2, int(N**0.5 + 1)):
        if primes[i]:
            j = 2
            while i * j < N:
                primes[i*j] = 0
                j += 1
    return [i for i, x in enumerate(primes) if x == 1]


def is_prime(n):
    primes = PRIMES_SET
    if n <= 10**8:
        return n in primes
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i:
            return False
    print('found a big prime: ', n)
    return True


def is_prime_pair(x, y):
    return is_prime(int('%s%s' % (x, y))) and is_prime(int('%s%s' % (y, x)))


def find_primes_pairs():
    """find pairs of two primes that concatenate into a prime."""
    subset = PRIMES[:1100]  # this value needed some tweaking
    primes = PRIMES_SET
    return set(
        (x, y)
        for x, y in combinations(subset, 2)
        if x != y and is_prime_pair(x, y)
    )


def find_remarkable_primes(primes_pairs, size=4):
    primes_with_prime_pair = defaultdict(list)
    for pair in primes_pairs:
        primes_with_prime_pair[pair[0]].append(pair[1])
        primes_with_prime_pair[pair[1]].append(pair[0])

    candidates = {
        x: set(y)
        for x, y in primes_with_prime_pair.items()
        if len(set(y)) >= size - 1
    }

    ret = []
    for x in candidates:
        for y in candidates[x]:
            if y in candidates:
                if len((set(candidates[y]) | set([y])) & (candidates[x] | set([x]))) >= size:
                    ret.append(tuple(sorted(list((set(candidates[y]) | set([y])) & (candidates[x] | set([x]))))))

    return min(
        (sum(x), x)
        for x, y in Counter(ret).items()
        if y >= size and all(is_prime_pair(u, v) for u, v in combinations(x, 2))
    )

if __name__ == '__main__':
    global PRIMES, PRIMES_SET
    with open('PRIMES_10_8', 'r') as f:
        PRIMES = list(int(x) for x in f.read().split('\n') if x)
        PRIMES_SET = set(PRIMES)

    assert is_prime_pair(3, 7)
    assert is_prime_pair(3, 109)
    assert is_prime_pair(3, 673)
    assert is_prime_pair(7, 109)
    assert is_prime_pair(7, 673)
    assert is_prime_pair(109, 673)
    print('checks done')
    print(find_remarkable_primes(find_primes_pairs(), size=5))
