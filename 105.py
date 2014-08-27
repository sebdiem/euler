
import itertools

def testCondition1(s):
    """
        Tests the following condition:
        S(B) != S(C); that is, sums of subsets cannot be equal.
    """
    sums = []
    for i in range(1, len(s)):
        s1 = itertools.combinations(s, i)
        for els1 in s1:
            if sum(els1) in sums: return False
            sums.append(sum(els1))
    return True

assert testCondition1([81, 88, 75, 42, 87, 84, 86, 65]) == False
assert testCondition1(sorted([157, 150, 164, 119, 79, 159, 161, 139, 158])) == True
   
def testCondition2(s):
    """
        Tests the following condition:
        If B contains more elements than C then S(B) > S(C)
        Note: assumes that s is sorted
    """
    for i in range(2, (len(s)+1)/2+1):
        if sum(s[:i]) <= sum(s[-i+1:]): return False
    return True

assert testCondition2(sorted([157, 150, 164, 119, 79, 159, 161, 139, 158])) == True
   
def problem105():
    f = open("sets.txt")
    result = 0
    for line in f:
        l = sorted([int(i) for i in line.split(",")])
        if testCondition1(l) and testCondition2(l):
            result += sum(l)
    f.close()
    return result

print problem105()

