class Tree:
    def __init__(self, value, *children):
        '''Singly linked tree, children do not know who their parent is.
        '''
        self.value = value
        self.children = tuple(children)

    @property
    def arguments(self):
        return (self.value,) + self.children

    def __eq__(self, tree):
        return self.arguments == tree.arguments

    def __repr__(self):
        argumentStr = ', '.join(map(repr, self.arguments))
        return '%s(%s)' % (self.__class__.__name__, argumentStr)


def init_tree(d1, d2):
    if d1 == 5: candidates = (1, 3, 5, 7, 9)
    else: candidates = (1, 3, 7, 9)
    children = [Tree((i,)) for i in candidates if i*d2 % 10 == d1]
    base_tree = Tree(0, *children)
    return base_tree, children

def extend_children(children, t1, t2):
    """t1 is a tuple with the last digits of p1,
    t2 is a tuple with the last digits of p2."""
    next = []
    for child in children:
        #s = sum((d*t2[i] for i, d in enumerate(child.value))) % 10
        q = sum((d*10**i for i, d in enumerate(child.value)))
        r2 = sum((d*10**i for i, d in enumerate(t2[::-1])))
        try:
            s = int(str(q*r2)[::-1][len(t1)-1])
        except IndexError:
            s = 0
        new_children = []
        for i in range(10):
            if (s + i*t2[-1]) % 10 == t1[0]:
                new_children.append(Tree(tuple(list(child.value)+[i,])))
        if new_children:
            child.children = tuple(new_children)
            next += new_children
    return next
            
def find_factor(p1, p2):
    s1, s2 = [int(c) for c in str(p1)], [int(c) for c in str(p2)]
    base_tree, children = init_tree(s1[-1], s2[-1])
    for i in range(2, len(s1)+1):
        children =  extend_children(children, s1[-i:], s2[-i:])
        if not children:
            print 'Problem...'
    if len(children) > 1:
        print p1, p2, children
    return min((c.value[::-1] for c in children))

def find_prime_pair_connection(p1, p2):
    factor = find_factor(p1, p2)
    result = sum([f*10**i for i, f in enumerate(factor[::-1])])*p2
    assert str(result)[-len(str(p1)):] == str(p1)
    return result

def dummy_solution(p1, p2):
    i = 2
    current = i*p2
    while str(current)[-len(str(p1)):] != str(p1):
        i += 1
        current = i*p2
    return current

def is_prime(n):
    if n == 2 or n == 3: return True
    i = 2
    while i <= n**0.5:
        if not n%i: return False
        i += 1
    return True

assert is_prime(11)
assert is_prime(13)
assert is_prime(101)
assert not is_prime(20)
assert not is_prime(27)
assert not is_prime(25)

import numpy as np
try:
    PRIMES = np.loadtxt('PRIMES.txt', dtype=np.int32)
except Exception:
    PRIMES = [n for n in range(5, int(1.01*10**6)) if is_prime(n)]
    np.savetxt('PRIMES.txt', PRIMES)

print 'all PRIMES found'

for i in range(100):
    p1 , p2 = (PRIMES[i], PRIMES[i+1])
    assert dummy_solution(p1, p2) == find_prime_pair_connection(p1, p2)

p1, p2 = PRIMES[10000], PRIMES[10001]
print p1, p2, find_prime_pair_connection(p1, p2)

print sum([find_prime_pair_connection(PRIMES[i], PRIMES[i+1]) for i in xrange(len(PRIMES)-1)
                                                              if 5<= PRIMES[i] < 10**6])

# En fait on dirait qu'on peut se passer d'arbre et qu'a chaque etape il n'y a qu'une seule
# possibilite pour le chiffre du facteur. Je n'ai pas cherche pourquoi...
