from fractions import gcd

def period(n, sq_n, p, current, seen):
    # p stores the digits of the continued fraction sequence
    # current enables to retrieve the current value of the "remainder": a/(sqrt(n)-b)
    # seen stores the old values of current to detect periodicity
    a, b = current
    sq_diff = n-b**2
    g = gcd(sq_diff, a)
    temp = int(a*(sq_n+b)/(n-b**2))
    current = (sq_diff/g , -((a/g)*b) + temp*(sq_diff/g))
    if current in seen: return tuple(p)
    p.append(temp)
    seen.append(current)
    return period(n, sq_n, p, current, seen)

#print period(23,24**0.5,[],(1,4))    

def continued_frac(n):
    sq_n = n**0.5
    sq_n_trunc = int(sq_n)
    result = [sq_n_trunc, tuple()]
    if sq_n != sq_n_trunc:
        result[1] = period(n, sq_n, [], (1, sq_n_trunc), [])
    return result

#print "\n".join(map(lambda x: str(x), [(i, continued_frac(i)) for i in range(2, 24)]))

def problem64():
    f = continued_frac
    return sum([1 for i in range(2, 10001) if len(f(i)[1])%2])

print problem64()        
        
