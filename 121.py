from itertools import combinations

def C(n,k):
    if k == 0 or n == k: return 1
    return (n*C(n-1, k-1))/k

def Pblue(t, k):
    """ Gives the probability to take blue disks at turns in t in a game of k turns """
    result = 1.
    for i in range(1, k+1):
        if i in t: result *= 1./(i+1)
        else: result *= i/(i+1.)
    return result

def P(n, k):
    """ Gives the probability to take n blue disks in k turns """
    result = 0
    for i in combinations(range(1, k+1), n):
        result += Pblue(i, k)
    return result

def problem121(N=15):
    x = sum((P(i, N) for i in range(N/2+1, N+1)))
    x = (1-x)/x
    return int(x) + 1 if int(x) != x else int(x) 

print "N=4: ", problem121(4)
print "N=15: ", problem121()
print "N=20: ", problem121(20)
