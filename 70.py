#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Sébastien Diemer <sebastien.diemer@mines-paristech.fr>

"""
Problem 70
"""

def is_permutation(m, n):
    s1, s2 = str(m), str(n)
    result = all((s1.count(c) == s2.count(c) for c in s1))
    if result: print m, n
    return result

assert is_permutation(87109, 79180)
assert not is_permutation(12345, 12346)
assert not is_permutation(66088, 66089)
assert is_permutation(66098, 66089)
assert not is_permutation(40697, 40696)
assert not is_permutation(84499, 84498)

def memo(f):
    def memoized_f(*args):
        if memoized_f._memo.has_key(args): return memoized_f._memo[args]
        else:
            result = f(*args)
            memoized_f._memo[args] = result
            return result
    memoized_f._memo = {}
    return memoized_f

@memo
def prime_factors(n):
    i = 2
    while i*i <= n:
        if not n%i:
            d = prime_factors(n/i).copy()
            d[i] = d.get(i, 0) + 1
            return d
        i += 1
    return {n:1}

def get_prime_factors(n):
    return [prime_factors(n) for n in xrange(2, n+1)]

from operator import mul



PRIMES = [2, 3]
@memo
def euler_function2(n):
    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 2
    for i in PRIMES:
        exp, j = 0, n
        while j and (not j%i):
            exp += 1
            j = j/i
        if exp:
            return (i**exp - i**(exp-1))*euler_function2(n/(i**exp))
    PRIMES.append(n)
    return n - 1


#print problem70()

import numpy as np
def build_primes(N=10**7):
    primes = np.ones(N)
    primes[0] = 0
    primes[1] = 0
    for i in xrange(2, int(N**0.5 + 1)):
        if primes[i]:
            j = 2
            while i*j < N:
                primes[i*j] = 0
                j += 1
    return primes

PRIMES = build_primes(10000000)
print "Done with PRIMES"
def is_prime(n):
    return PRIMES[n] == 1

assert is_prime(13)
assert is_prime(17)
assert not is_prime(21)


def build_prime_factors():
    N = len(PRIMES)
    factors = [[] for _ in xrange(N)]
    for i, is_prime in enumerate(PRIMES):
        if is_prime:
            j = 1
            while i*j < N:
                factors[i*j].append(i)
                j += 1
    return factors

FACTORS = build_prime_factors()
print "Done with factors"

def prime_factors(n):
    return FACTORS[n]

assert prime_factors(2) == [2]
assert prime_factors(4) == [2]
assert prime_factors(6) == [2, 3]
assert prime_factors(90) == [2, 3, 5]

def euler_function2(n):
    if n == 1: return 1
    factors = prime_factors(n)
    return (n*reduce(mul, [f-1 for f in factors]))/reduce(mul, factors)

assert euler_function2(2) == 1
assert euler_function2(3) == 2
assert euler_function2(91) == 72

def problem70():
    mini, value = 10, -1
    for n in xrange(2, 10000000):
        euler = euler_function2(n)
        if is_permutation(n, euler):
            if float(n)/euler < mini:
                mini, value = float(n)/euler, n
    return value

print problem70()
