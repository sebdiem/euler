#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Sébastien Diemer <sebastien.diemer@mines-paristech.fr>

"""
L'idée de cette solution repose sur la fonction Totient d'euler, qui compte
le nombre d'entiers inférieurs à n et premiers avec n.
Cette fonction vaut n-1 pour n premier, est multiplicative entre deux nombres
premiers entre eux.
"""
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

def euler_product(factors):
    return reduce(mul, [f**i - f**(i-1) for f, i in factors.items()])

def count_fractions(d_max=8):
    factors = get_prime_factors(d_max)
    return sum([euler_product(f) for f in factors])

print count_fractions(1000000)
