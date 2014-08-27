memo = {}
def chain(n):
    if n == 1: return 1
    if memo.has_key(n):
        return memo[n]
    if n%2:
        memo[n] = 1 + chain(3*n+1)
    else:
        memo[n] = 1 + chain(n/2)
    return memo[n]
        
        
def longest_chain(N):
    best = 10
    bestn = 13
    for i in xrange(1,N):
        n = chain(i)
        if n > best:
            best = n
            bestn = i
    return bestn
print longest_chain(10**6)


