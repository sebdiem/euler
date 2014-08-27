def digit(n):
    k = 1
    while sum([9*10**(i-1)*i for i in range(1, k+1)])  < n:
        k += 1
    s = sum([9*10**(i-1)*i for i in range(1, k+1)]) + 1
    return int(str(10**k + (n-s)/k)[(n-s)%k])
    
print reduce(lambda x,y: x*y, [digit(10**i) for i in range(7)])
