memo = {}
def Comb(n,k):
    if n == k or k == 0: return 1
    if memo.has_key((n,k)): return memo[(n,k)]
    result = (n*Comb(n-1,k-1)/k)
    memo[(n,k)] = result
    return result

result = 0
for n in range(1, 101):
    for k in range(3,n-1):
        if Comb(n,k) > 10**6:
            result += 1
print result
