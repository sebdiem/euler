import sys
import random
def nearest_power_of_ten(n):
    # returns the power of ten just below or equal n
    k = 0
    while 10**k <= n:
        k += 1
    k -= 1
    return k

def decompose(n, k=-1):
    if k < 0: k = nearest_power_of_ten(n)
    n_list = []
    temp = n
    for i in range(k+1):
        n_list.append(int(temp/10**(k-i)))
        temp -= n_list[-1]*(10**(k-i))
    return n_list

def calculate(n_list):
    l = len(n_list)
    return sum([k*10**(l-i-1) for i,k in enumerate(n_list)])

def f(n, d=1, skip=False):
    k = nearest_power_of_ten(n)
    if skip:
        if n > (k+1)*10**k: return (k+1)*10**k
        if n < (k*10**(k-1)): return (k*10**(k-1))
    result = 0
    n_list = decompose(n, k)
    l = len(n_list)
    for i,k in enumerate(n_list):
        if k == d:
            result += 1 + k*(l-1-i)*(10**(l-2-i))
            result += calculate(n_list[i+1:])
        elif k > d:
            result += 10**(l-1-i) + k*(l-1-i)*(10**(l-2-i))
        elif k > 0:
            result += k*(l-1-i)*(10**(l-2-i))
    return int(result)

def alt_f(n, d):
    return sum([str(i).count(str(d)) for i in xrange(n+1)])

def time_it(f, *args):
    start = time.clock()
    f(*args)
    return (time.clock() - start)*1000

print decompose(1000)
print calculate(decompose(1000))

def test_f():
    n_list = [random.randint(1,10000) for i in range(100)]
    for d in range(1,10):
        for n in n_list:
            if f(n, d) != alt_f(n, d):
                print n, f(n, d), alt_f(n, d)
                raise
    print "test pass"

results = []
for d in range(1,10):
    i = 1
    result = 0
    while i <= 100000000000000:
        fi = f(i, d, True)
        step = max(1, abs(fi-i)/max(150, str(i).count(str(d))))
        if fi == i:
            result += i
            print result  
        i += step
    results.append(result)

print results, sum(results)
