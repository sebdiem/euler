
def square_laminae(N):
    total = 0
    for n in range(2, N+1):
        limit = int(((n-1)**2 + N)**0.5)-n+2
        for m in range(1, limit):
            if 4*m*(n+m-1) < N+1:
                total += 1
    return total
   
print square_laminae(10**6)

