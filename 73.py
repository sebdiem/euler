#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Sébastien Diemer <sebastien.diemer@mines-paristech.fr>

"""

"""
from __future__ import division
from operator import mul
from fractions import gcd

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

assert prime_factors(5) == {5:1}
assert prime_factors(2) == {2:1}
assert prime_factors(3) == {3:1}
assert prime_factors(3) == {3:1}
assert prime_factors(8) == {2:3}
assert prime_factors(18) == {2:1, 3:2}

def is_divisible_by_any(n, factors):
    return not bool(reduce(mul, [n%f for f in factors]))

assert is_divisible_by_any(8, [2, 3]) == True

def reduced_fractions(d_max=12000):
    return [(n, d) for d in xrange(2, d_max+1)
                   for n in xrange(d//3+1, d//2+1)
                   if not is_divisible_by_any(n, prime_factors(d).keys())]

def sort_fractions(fractions):
    return sorted(fractions, key=lambda t: t[0]/t[1])

def count_fractions_between(fractions):
    sorted_frac = sort_fractions(fractions)
    if sorted_frac[0] == (1, 3): sorted_frac = sorted_frac[1:]
    if sorted_frac[-1] == (1, 2): sorted_frac = sorted_frac[:-1]
    return len(sorted_frac)

assert count_fractions_between(reduced_fractions(8)) == 3

def problem_73():
    fractions = reduced_fractions()
    return count_fractions_between(fractions)

print "La solution est ", problem_73()
