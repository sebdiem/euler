i = 828427094427
"""
while i < 10**13:
    p = (i-1)*(i+1)
    if not p%8:
        sq = (p/8)**0.5 
        if int(sq) == sq:
            b = (2*sq + 1 + i)/2
            print i, sq, b, b+sq, (b*(b-1))/((b+sq)*(b+sq-1.))
    i += 1"""

p = 10**12
while True:
    sq = (8*p**2-4*p+1)**0.5
    if sq == int(sq):
        q = 1 - p - int(sq)
        b, r = (p+q)/2, (p-q)/2
        if b>0 and r>0:
            print p, q, b, r
            break
    p += 1
