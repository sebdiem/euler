
import itertools

def testCondition1(s):
    sums = []
    for i in range(1, len(s)):
        s1 = itertools.combinations(s, i)
        for els1 in s1:
            if sum(els1) in sums: return False
            sums.append(sum(els1))
    return True
   
print testCondition1([1,2,3])
print testCondition1([2,3,4]) 
print testCondition1([3,5,6,7]) 
print testCondition1([6,9,11,12,13])  

def brute():
    best = 10**6
    for a1 in range(6,100):
        for a2 in range(a1+1,100):
            for a7 in range(a1+7, a1+a2):
                for a3 in range(a2+1, a7):
                    for a6 in range(a1+6, a1+a2+a3-a7):
                        for a4 in range(a3+1, a6):
                            for a5 in range(a1+5, a1+a2+a3+a4-a7-a6):
                                t = (a1,a2,a3,a4,a5,a6,a7)
                                if sum(t) < best and a1<a2<a3<a4<a5<a6<a7 and \
                                   testCondition1(t):
                                    print t
                                    best = sum(t)                                   
                                   
                                   
brute()

