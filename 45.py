N = 10**5
candidates_pent = set([int((-1+(1+4*p*(3*p-1))**0.5)/2) for p in xrange(1, N)
            if (-1+(1+4*p*(3*p-1))**0.5)/2 == int((-1+(1+4*p*(3*p-1))**0.5)/2)])
candidates_hex = set([int((-1+(1+8*q*(2*q-1))**0.5)/2) for q in xrange(1, N) 
            if (-1+(1+8*q*(2*q-1))**0.5)/2 == int((-1+(1+8*q*(2*q-1))**0.5)/2)])

triangle = lambda x: (x*(x+1))/2
results = list(candidates_pent.intersection(candidates_hex))
print triangle(results[results.index(285)+1])
