"""On exploite: si n divisible par a alors R(n) divisible par R(a)"""
def is_prime(n):
    if n == 2 or n == 3: return True
    i = 2
    while i <= n**0.5:
        if not n%i: return False
        i += 1
    return True

assert is_prime(11)
assert is_prime(101)
assert is_prime(37)
assert not is_prime(16)
assert not is_prime(20)

def decompose_primes(n):
    d = {}
    k, i = n, 2
    while k > 1 and i <= n**0.5:
        if not k%i:
            if d.has_key(i): d[i] += 1
            else: d[i] = 1
            k = k/i
        else:
            i += 1
    if k!= 1:
        if d.has_key(k): d[k] += 1
        else: d[k] = 1
    return d

assert decompose_primes(11) == {11: 1}
assert decompose_primes(20) == {2: 2, 5: 1}

print decompose_primes(10**9)

#print [n for n in xrange(10000) if is_prime(n) if str(n)[-1] == '1']
#print '\n'.join(['%s, %s : %s' % (i, '1'*i,  str(decompose_primes(int('1'*i))))
#                 for i in xrange(2, 17)])

print decompose_primes(int('1'*20))
print decompose_primes(int('1'*25))

#from sets import Set
#s = Set()
#i = 2
#while len(s) < 40:
#    for k in decompose_primes(int('1'*i)):
#        s.add(k)
#    print i, len(s)
#    i += 1
#print s
