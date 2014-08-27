N = 10**7

NB_OF_DIV = [0]*N

for i in range(2, N):
    j = 1
    p = i*j
    while p <= N:
        NB_OF_DIV[p-2] += 1
        j += 1
        p = i*j

print sum([NB_OF_DIV[i] == NB_OF_DIV[i+1] for i in range(len(NB_OF_DIV)-1)])
