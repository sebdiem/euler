
def square_laminae(N):
    result = {}
    for n in range(2, N+1):
        limit = int(((n-1)**2 + N)**0.5)-n+2
        for m in range(1, limit):
            if 4*m*(n+m-1) < N+1:
                if result.has_key(4*m*(n+m-1)): result[4*m*(n+m-1)] += 1
                else: result[4*m*(n+m-1)] = 1
    return result
   
def problem174():
    sl = square_laminae(10**6)
    N = lambda n: sum((1 for s in sl if sl[s] == n))
    return sum((N(i) for i in range(1,11)))
   
print problem174()

