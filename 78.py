memo = {}
def k_partitions(n, k):
    # number of partitions of n with k elements
    if k == 1: return 1
    if k == n: return 1
    if k > n: return 0
    if memo.has_key((n,k)): return memo[(n,k)]
    result = k_partitions(n-1, k-1) + k_partitions(n-k, k)
    memo[(n,k)] = result
    return result

def partitions(n):
    return sum([k_partitions(n,k) for k in range(1,n+1)])

print partitions(5)
print partitions(10)

N = 10**4
PENTAG = [((k*(3*k-1))/2,k) for k in range(1, N+1)] + \
         [((-k*(-3*k-1))/2,k) for k in range(1, N+1)]
PENTAG.sort()

memo2 = {}
def partitions2(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 3
    if n == 4: return 5
    if memo2.has_key(n): return memo2[n]
    result = 0
    for p,k in PENTAG:
        if p > n: break
        result += ((-1)**(k+1))*partitions2(n-p)
    memo2[n] = result
    return result

print partitions2(5)
print partitions2(10)

def problem78():
    n = 1
    while True:
        p = partitions2(n)
        if not p%10**6: return n
        n += 1

print problem78()
