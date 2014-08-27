import itertools

def is_prime(n):
    if n == 1 or n == 0: return False
    if n == 2 or n == 3: return True
    i = 3
    while i <= n**0.5:
        if not n%i: return False
        i += 2
    return True

all_units = [1,3,7,9]

def pandigit_prime(n):
    units = [u for u in all_units if u <= n]
    best = 0
    powers = [10**i for i in range(1,n)]
    for u in units:
        ran = range(1,n+1)
        ran.remove(u)
        for p in itertools.permutations(ran):
            can = u+sum([a*b for a,b in zip(p, powers)])
            if can > best:
                if is_prime(can):
                    best = can
    return best

def problem41():
    best = 0
    for n in range(1, 9):
        c = pandigit_prime(n)
        if c: best = c
    return best

print problem41()
            
        
