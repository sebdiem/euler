import math
import fractions
import time

def lcm(a,b): return abs(a * b) / fractions.gcd(a,b) if a and b else 0
def number_of_dividers(n):
    if n == 0: raise
    if n == 1: return 1
    result = 0
    for i in range(1,(n+1)/2 + 1):
        if not n%i: result += 1
    return result + 1 # n divides n

print "mlkj",number_of_dividers(25)

N = 10**7

def find_sq_matrices(N):
    result = 0
    start = lambda x: x%2 if x%2 else 2
    for X in range(2, int(math.sqrt(2*N-1))+1):
        X_sq = X**2
        print X
        for Y in range(start(X), min(X, int(math.sqrt(2*N - X_sq))+1), 2):
            Y_sq = Y**2
            if X_sq + Y_sq < 2*N:
                A_plus_D = X_sq + Y_sq
                k = (X_sq - Y_sq)/4
                ppcm0 = lcm(X,Y)
                ppcm = ppcm0**2
                for i in range(1, min(X_sq*(X_sq-4*k)/(4*ppcm), Y_sq*(Y_sq+4*k)/(4*ppcm)) + 2):
                    b1c1 = i*ppcm/X_sq
                    b2c2 = i*ppcm/Y_sq
                    a1d1 = k + b1c1
                    a2d2 = -k + b2c2
                    if a2d2 > 0 and X_sq >= 4*a1d1 and Y_sq >= 4*a2d2:
                        sq1 = math.sqrt(X_sq - 4*a1d1)
                        if sq1 == int(sq1) and sq1%2 == X%2:
                            sq1 = int(sq1)
                            sq2 = math.sqrt(Y_sq - 4*a2d2)
                            if sq2 == int(sq2) and sq2%2 == Y%2:
                                sq2 = int(sq2)
                                a11 = (X + sq1)/2
                                a12 = (X - sq1)/2
                                a21 = (Y + sq2)/2
                                a22 = (Y - sq2)/2
                                nd = number_of_dividers(i)
                                result += (nd) if a11 == a12 else 2*(nd)
                                #print X, Y, ppcm, k, b1c1, b2c2, a11, a12, a21, a22, a1d1, a2d2, i, nd                
    return result
start = time.time()
print find_sq_matrices(N)
print "time: ", time.time()-start
