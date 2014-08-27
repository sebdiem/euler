
def possibleDarts(n):
    result = []
    if n == 0: return [str(-1)]
    if n == 50: return ["D25"]
    if n == 25: return ["S25"]
    if not n%2 and n/2 <=20: result.append("D%d" % (n/2))
    if not n%3 and n/3 <= 20: result.append("T%d" % (n/3))
    if n <= 20: result.append("S%d" % n)
    return result

def possibleTwoDarts(n):
    if n > 120: return []
    if n == 0: return [("-1","-1")]
    result = []
    for i in range((n+1)/2, n+1):
        darts1, darts2 = possibleDarts(i), possibleDarts(n-i)
        for d1 in darts1:
            for d2 in darts2:
                if not (d2, d1) in result:
                    result.append((d1,d2))
    return result
                                                           
def checkouts(n):
    s = set()
    ext = [25] if n >= 50 else []
    for double in range(1, min((n+1)/2+1, 21))+ext:
        p = possibleTwoDarts(n-2*double)
        s |= set([("D%d" % double,) + el for el in p])
    return len(s)

assert checkouts(6) == 11
   
def problem109(N=100):
    return sum(checkouts(n) for n in range(2, N))

assert problem109(171) == 42336
print problem109()

