#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Sébastien Diemer <sebastien.diemer@mines-paristech.fr>

"""

"""

def is_prime(n):
    if n == 2 or n == 3: return True
    i = 2
    while i*i <= n:
        if not n%i: return False
        i += 1
    return True

assert is_prime(13)
assert is_prime(17)
assert not is_prime(28)

def decompose(n):
    s = str(n)
    return [(int(s[:i]), int(s[i:])) for i in xrange(1, len(s)) if s[i] != '0']

assert decompose(7109) == [(7, 109), (710, 9)]


PRIMES = {}
N = 300000
for n in xrange(2, N):
    if not n in PRIMES:
        if is_prime(n):
            PRIMES[n] = tuple()
            for p, q in decompose(n):
                if p in PRIMES and q in PRIMES:
                    m = int('%d%d' % (q, p))
                    if m < n:
                        if m in PRIMES:
                            # p, q can be put together to form two new primes
                            # we discovered one new 'match' for each:
                            PRIMES[p] += (q,)
                            PRIMES[q] += (p,)
                    elif is_prime(m):
                        PRIMES[m] = tuple()
                        # p, q can be put together to form two new primes
                        # we discovered one new 'match' for each:
                        PRIMES[p] += (q,)
                        PRIMES[q] += (p,)
                
from itertools import combinations

def test_five(five_primes):
    for e1, e2 in combinations(five_primes, 2):
        if e1[0] in e2[1] and e2[0] in e1[1]:
            pass
        else:
            i1, i2 = int('%d%d' % (e1[0], e2[0])), int('%d%d' % (e2[0], e1[0]))
            if i1 > N and i2 > N:
                if is_prime(i1) and is_prime(i2):
                    pass
                else:
                    return False
            else: return False
    return True

test = [p for p in PRIMES[3] if p in PRIMES[7]]
print test
for t1, t2 in combinations(test, 2):
    i1, i2 = int('%d%d' % (t1, t2)), int('%d%d' % (t2, t1))
    if is_prime(i1) and is_prime(i2):
        print t1, t2
print is_prime(int('%d%d' % (9901, 673)))
print is_prime(int('%d%d' % (673, 9901)))
#for el in combinations([(p, q) for p, q in PRIMES.items() if len(q) > 2], 5):
#    print el[1]
    #if test_five(el):
    #    print [e[0] for e in el]
    #    break
            
