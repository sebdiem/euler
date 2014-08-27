# -*- coding: utf-8 -*-

def decompose(n, d):
    if n == 1: return d
    for i in xrange(2, int(n**0.5)+1):
        if not n%i:
            if d.has_key(i): d[i] += 1
            else: d[i] = 1
            return decompose(n/i, d)
    if d.has_key(n): d[n] += 1
    else: d[n] = 1
    return d

print decompose(2, dict())
print decompose(3, dict())
print decompose(4, dict())
print decompose(5, dict())
print decompose(6, dict())
print decompose(7, dict())
print decompose(8, dict())
print decompose(9, dict())
print decompose(10, dict())

def minimal_solution(D):
    if any([pow>1 for pow in decompose(D, dict()).values()]):
        #print 'Not necessary for ', D
        print D, ' ok'
        return 0
    # x^2 = 1%D
    for k in xrange(1, 1000000000):
        x_2 = k**2*D + 1
        x = int(x_2**0.5)
        if x**2 == x_2:
            #print '%s^2 - %s x %s^2 = 1' % (x, D, k)
            print D, ' ok'
            return x
    print 'No solution found for ', D

def problem66():
    return max([minimal_solution(D) for D in xrange(2, 1001)])

x = problem66()
print 'Solution: ', x

#Dy^2 = (x-1)(x+1)
#Si D est pair, x est impair
#Facteurs communs de k et k+2?
#2 si k est pair mais c'est le seul possible
#En effet: si m > 2 est un diviseur de k: k%m = 0 => (k+2)%m = 2 != 0
#Réciproquement si m > 2 est un diviseur de k + 2: (k+2)%m = 0 => k%m = m-2 != 0
#Donc si k est impair, k et k+2 premiers entre eux, sinon 2 est le seul facteur commun
#Or y^2 divise (x-1)(x+1) si y = p1^i1 x p2^i2 x ... x pN^iN alors y^2 = p1^2*i1 x ...
#Donc la décomposition en facteurs premiers de x-1 et x+1 se compose de:
#* facteurs premiers à une puissance paire
#* des facteurs de D


#D = 1000 = 2^3 * 5^3
# x-1 = 2^3 x s1(y^2), x+1 = 5^3 x s2(y^2)

#(x^2-y^2) - (D-1)y^2 = 1
#(x-y)(x+y) - (D-1)y^2 = 1
