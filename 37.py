
memo = {}
def is_prime(n):
    if n == 1 or n == 0: return False
    if n == 2 or n == 3: return True
    if memo.has_key(n): return memo[n]
    i = 2
    while i <= n**0.5:
        if not n%i:
            memo[n] = False
            return False
        i += 1
    memo[n] = True
    return True

   
def problem37():
    result = []
    i = 11
    while len(result) < 11:
        s = str(i)
        if is_prime(i):
            truncatable_prime = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])) or not is_prime(int(s[:-j])):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                result.append(i)
        i += 2
    return result
"""   
r = problem37()
print r, sum(r)"""

 # Deuxieme solution plus rapide et qui ne suppose pas qu'il y a onze solutions:#

def list_to_int(l):
    if len(l) == 1: return l[0]
    return l[-1] + 10*list_to_int(l[:-1])  
   
def test_left(l):
    for i in range(len(l)):
        if not is_prime(list_to_int(l[:(len(l)-i)])):
            return False
    return True   

def test_right(l):
    for i in range(len(l)):
        if not is_prime(list_to_int(l[i:])):
            return False
    return True

def problem37bis():
    candidates_start = [2,3,5,7]
    candidates_end = [1,3,7,9]
    to_be_explored = [[c] for c in candidates_start]
    result = []
    while to_be_explored:
        next = to_be_explored.pop()
        if test_right(next): result.append(next)
        tree_continues = False
        for i in candidates_end:
            if test_left(next + [i]):
                to_be_explored.append(next + [i])
                tree_continues = True
        if not tree_continues and not next in result and test_right(next) :
            result.append(next)
    return sorted(map(lambda x: list_to_int(x), filter(lambda x: len(x)>1, result)))

r = problem37bis()
print r, len(r), sum(r)

