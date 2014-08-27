from operator import mul
def fact(n):
    if n == 0 or n == 1: return 1
    return reduce(mul, range(1, n+1))

assert fact(5) == 120

def comb(n, k):
    return fact(n)/(fact(k)*fact(n-k))

assert comb(10, 1) == 10
assert comb(5, 0) == 1
assert comb(6, 2) == 15

def count_prizes_with_late(days):
    return sum([count_prizes_without_late(days-l-1)*count_prizes_without_late(l)
                for l in range(days)])

def problem191(N=4):
    return count_prizes_without_late(N) + count_prizes_with_late(N)

def expand_tree(children):
    new = []
    for child in children:
        if len(child) > 1 and child[-2:] == (1, 1):
            new_children = [child + (0,)]
        else:
            new_children = [child + (0,), child + (1,)]
        new += new_children
    return new

def count_prizes_without_late(days):
    children = [(0,)]
    for i in range(days):
        children = expand_tree(children)
    return len(children)

count_prizes_without_late(10)

# after running the dummy version, we can see the following recurence:
# f(n) = 2*f(n-1) - f(n-4):

def count_prizes_without_late(days):
    if days < 4: return (1, 2, 4, 7)[days]
    if not hasattr(count_prizes_without_late, 'save'): count_prizes_without_late.save = dict()
    if count_prizes_without_late.save.has_key(days): return count_prizes_without_late.save[days]
    result = 2*count_prizes_without_late(days-1) - count_prizes_without_late(days-4)
    count_prizes_without_late.save[days] = result
    return result

assert count_prizes_without_late(4) == 13
assert problem191() == 43

print problem191(N=30)
