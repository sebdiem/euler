def is_pentagonal(n):
    delta = 1+24*n
    sq_delta = delta**0.5
    if sq_delta == int(sq_delta):
        if not (1+sq_delta)%6: return True
    return False

print is_pentagonal(1)
print is_pentagonal(5)
print is_pentagonal(12)
print is_pentagonal(22)
print is_pentagonal(35)
print is_pentagonal(51)
print is_pentagonal(70)
print is_pentagonal(92)
print is_pentagonal(117)
print is_pentagonal(145)
print is_pentagonal(122)
print is_pentagonal(23)

def problem44():
    n = 1
    pent = []
    while True:
        pent.append((n*(3*n-1))/2)
        pentn = pent[-1]
        for i in range(n-1):
            penti = pent[i]
            if is_pentagonal(penti+pentn) and is_pentagonal(pentn-penti):
                return pentn-penti
        n += 1

print problem44()
