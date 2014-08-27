import fractions

frac_list = reduce(lambda x,y: x+y, [[1,2*(i+1),1] for i in range(100)])[:99]
frac_list = [2] + frac_list

"""
# test for 2 
N = 4
frac_list = [1] + [2 for i in range(N)]"""

def continued_frac(l):
    if len(l) == 1: return  (1, l[0])
    r = l.pop(0)
    (p,q) = continued_frac(l)
    s = fractions.gcd(q, (q*r+p))
    return (q/s, (q*r+p)/s)

result = continued_frac(list(frac_list))[1] # we calculate the inverse
print sum([int(c) for c in str(result)])
