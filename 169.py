from math import log

def decompose(n, base=2):
    if n == 0: return [0]
    result = []
    k = int(log(n)/log(base))
    remain = n
    while k >= 0:
        d = remain/base**k
        result.append(d)
        remain -= d*base**k
        k -= 1
    return result

memo = {}
def solve(l):
    if len(l) == 0: return 1
    if len(l) == 1: return l[0] <= 2
    if memo.has_key(l): return memo[l]
    # find the next non zero power of two
    if 1 in l[1:]: k = l[1:].index(1)
    else: k = len(l) - 1
    if l[0] == 1:
        result = (k+1)*solve(l[k+1:]) + solve((3,) + l[k+2:])
    else: # here l[0] == 3
        if l[0] != 3: raise("problem")
        result = k*solve(l[k+1:]) + solve((3,) + l[k+2:])
    memo[l] = result
    return result

def problem169(N=10**25):
    d = tuple(decompose(N))
    return solve(d)

print problem169()


"""
    the following functions were used to compute a first algorithm:
    very slow but useful to check the correctness of other
    algorithms for small values
"""
def is_valid(l):
    return reduce(lambda x,y: x and y, [i <= 2 for i in l])

def find_next(l):
    result = []
    for i in range(1, len(l)):
        if l[i] > 3: return []
        if l[i] > 0 and (l[i-1] == 0 or (i > 1 and l[i-1] == 1 and l[i-2] <= 1)):
            temp = [el for el in l]
            temp[i] -= 1
            temp[i-1] += 2
            if temp[0] <= 2:
                result.append(temp)
    return result

def problem169_too_slow(n=10):
    d = decompose(n)
    d.reverse()
    frontier, seen = [d], []
    result = 0
    while frontier:
        current = frontier.pop()
        if is_valid(current):
            result += 1
        for next in find_next(current):
            if not next in seen:
                frontier.append(next)
        seen.append(current)
    return result

    
