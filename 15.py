memo = {}
def lat(i,j):
    if i*j == 0: return 1
    if memo.has_key((i,j)): return memo[(i,j)]
    if j > i:
        return lat(j,i)
    result = 0
    if j > 0:
        result = lat(i,j-1) + lat(i-1,j)
    else: result = lat(i-1,j)
    memo[(i,j)] = result
    return result
    
print lat(20,20)