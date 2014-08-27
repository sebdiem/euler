import itertools

results = []
for d1 in range(1, 10): # chiffre des unites du facteur 1
    digits = range(1,10)
    digits.remove(d1)
    for d2 in digits: # chiffre des unites du facteur 2
        digits2 = list(digits)
        digits2.remove(d2)
        d3 = int(str(d1*d2)[-1]) # chiffre des unites du produit
        if d3 in digits2:
            digits2.remove(d3)
            for d4,d5,d6,d7,d8,d9 in itertools.permutations(digits2):
                p = d7*10**3+d8*10**2+d9*10+d3
                if p == (d4*10**3+d5*10**2+d6*10+d1)*d2 or \
                   p == (d4*10**2+d5*10+d1)*(d6*10+d2):
                    if not p in results: results.append(p)

print sum(results)
