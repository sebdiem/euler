from fractions import gcd
def continued_fraction_2(N):
    n, d = (3, 2)
    for _ in xrange(N-1):
        n, d = 2*d + n, d + n
        k = gcd(n, d)
        n, d = n/k, d/k
    return n, d

assert continued_fraction_2(1) == (3, 2)
assert continued_fraction_2(2) == (7, 5)
assert continued_fraction_2(3) == (17, 12)
assert continued_fraction_2(4) == (41, 29)
assert continued_fraction_2(5) == (99, 70)
assert continued_fraction_2(6) == (239, 169)
assert continued_fraction_2(7) == (577, 408)
assert continued_fraction_2(8) == (1393, 985)

def problem57(N=1000):
    n, d = (3, 2)
    count = 0
    for _ in xrange(N-1):
        n, d = 2*d + n, d + n
        k = gcd(n, d)
        n, d = n/k, d/k
        if len(str(n)) > len(str(d)): count += 1
    return count

print problem57()

