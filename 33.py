from fractions import gcd

candidates = []
for i in range(1,10):
    for j in range(i+1, 10):
        candidates.append((i,j))

result = []
for c1, c2 in candidates:
    for k in range(1, 10):
        if c1*(10*c2+k) == c2*(10*k+c1): result.append((c1,c2))
        if c1*(10*k+c2) == c2*(10*c1+k): result.append((c1,c2))

r1,r2 = reduce(lambda x,y:(x[0]*y[0], x[1]*y[1]), result)
print r2/gcd(r1,r2)
    
