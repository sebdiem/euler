memo = {}
def is_prime(n):
    if n <= 0 or n == 1: return False
    if memo.has_key(n): return memo[n]
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            memo[n] = False
            return False
    memo[n] = True    
    return True

coeff = range(-999, 1000)

def max_succ(a,b):
    quad = lambda x: x**2+a*x+b
    n = 0
    while is_prime(quad(n)):
        n += 1
    return n


best = 0
best_coeffs = (0,0)
for a in coeff:
    print a
    for b in coeff:
        cand = max_succ(a,b)
        if cand > best:
            best = cand
            best_coeffs = (a,b)

print best_coeffs[0]*best_coeffs[1]
