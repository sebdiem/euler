from math import log

memoi = {}
def count_increasing_with_n_digits(n, sup=1):
    if n < 2: return 10-sup
    if memoi.has_key((n,sup)): return memoi[(n,sup)]
    result = 0
    for first_digit in range(sup, 10):
        result += count_increasing_with_n_digits(n-1, first_digit)
    memoi[(n,sup)] = result    
    return result

memod = {}
def count_decreasing_with_n_digits(n, inf=9, first=False):
    if inf == 0: return 1
    if n < 2: return inf+1
    if memod.has_key((n, inf, first)): return memod[(n, inf, first)]
    result = 0
    start = 1 if first else 0
    for first_digit in range(start, inf+1):
        result += count_decreasing_with_n_digits(n-1, first_digit)
    memod[(n, inf, first)] = result
    return result

def count_not_bouncy_with_n_digits(n):
    if n == 1: return 9
    return count_increasing_with_n_digits(n) + \
           count_decreasing_with_n_digits(n, first=True) - 9


def count_not_bouncy(limit=10**6):
    return sum([count_not_bouncy_with_n_digits(n) for n in range(1, int((log(limit)+0.0001)/log(10))+1)])

print count_not_bouncy(10**6)
print count_not_bouncy(10**10)
print count_not_bouncy(10**100)
