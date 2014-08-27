#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Sébastien Diemer <sebastien.diemer@mines-paristech.fr>

"""

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

def fac(n):
    if n < 2: return 1
    return n*fac(n-1)

FACTORIALS = [fac(i) for i in range(10)]

@memo
def sum_of_factorials(n):
    if n == 0: return 0
    return sum_of_factorials(n/10) + FACTORIALS[n%10]

assert sum_of_factorials(145) == 145
assert sum_of_factorials(169) == 363601
assert sum_of_factorials(363601) == 1454
assert sum_of_factorials(871) == 45361

def chain_length(n):
    chain = [n]
    while True:
        next = sum_of_factorials(chain[-1])
        if next in chain:
            return len(chain)
        else:
            chain.append(next)

assert chain_length(69) == 5
assert chain_length(145) == 1
assert chain_length(78) == 4

def problem_74(length=60):
    return sum([(chain_length(i) == length) for i in xrange(1, 1000000)])

print "The solution is: ", problem_74()
