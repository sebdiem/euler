#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Sébastien Diemer <sebastien.diemer@mines-paristech.fr>

"""
Problem 80
"""

def has_irrational_sqrt(n):
    return int(n**0.5)**2 != n

def next_continued_fraction_coeffs(target_sqrt, num, denom):
    m = int((target_sqrt**0.5 + num)/denom)
    num = -num + m*denom
    denom = (target_sqrt - num**2)/denom
    return m, num, denom

def continued_fraction_of_sqrt(n, length=200):
    result, num, denom = [], 0, 1
    for _ in xrange(length):
        m, num, denom = next_continued_fraction_coeffs(n, num, denom)
        result.append(m)
    return result

def rational_continued_fraction(f):
    num, denom = 1, f[-1]
    for el in f[::-1][1:]:
        temp = denom
        denom = num + el*denom
        num = temp
    return denom, num # the last step of the algorithm makes one extra inversion

def approximate_sqrt(n):
    f = continued_fraction_of_sqrt(n)

def find_n_digit_rational(n, num, denom):
    current = num%denom
    result = [num/denom]
    remaining_digits = n-len(str(result[0]))
    for _ in xrange(remaining_digits):
        result.append((current*10)/denom)
        current = (current*10)%denom
    return result

def sum_n_digit(n, integer):
    frac = continued_fraction_of_sqrt(integer, length=2*n)
    rat = rational_continued_fraction(frac)
    return sum(find_n_digit_rational(n, *rat))

a, b = rational_continued_fraction(continued_fraction_of_sqrt(2))
assert sum(find_n_digit_rational(100, a, b)) == 475

def problem80():
    return sum([sum_n_digit(100, i) for i in xrange(100) if has_irrational_sqrt(i)])

print problem80()
