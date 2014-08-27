memo = {}
def factors(n):
    if n == 1: return set()
    if memo.has_key(n): return memo[n]
    i = 2
    result = set()
    prime = True
    while i <= n**0.5:
        if not n%i:
            result.add(i)
            result |= factors(n/i)
            prime = False
            break
        i += 1
    if prime: result.add(n)
    return result


def problem47(rank=4):
    n = 1
    while True:
        lengths = [len(factors(n+r)) for r in range(rank)]
        if lengths[0] == rank and lengths.count(lengths[0]) == rank: break
        n += 1
    return n

print problem47()
