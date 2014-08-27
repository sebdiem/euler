from fractions import gcd
results = []
MAX = 10**6
"""MAX 10**4:
(4283, 9994)
(4285, 9998)
MAX 10**5:
(42854, 99993)
(42856, 99997)
"""
for n in xrange(1, MAX):
    print n
    for d in xrange(int(99997./42856*n), min(int(99993./42854*n)+1, MAX)):
        if gcd(n, d) == 1:
            results.append((n, d))

results.sort(key=lambda x: x[0]/float(x[1]))
print results[results.index((3, 7)) - 1]
print results[results.index((3, 7)) + 1]
