""" Le principe est le suivant:
    on fait la récurrence suivante n est égal à:
    n-1 + 1
    n-2 + 2
    ...
    1   + (n-1)
Pour éviter les répétitions il faut que les nombres de la colonne de droite soit décomposées
avec des nombres plus petits ou égaux que le nombre correspondant de la colonne de gauche."""
d = dict()
def count_with_max(n, max_term):
    """Count ways to write n using terms <= max_ter."""
    if max_term == 1: return 1
    if n == 1: return 1
    if max_term >= n: return 1 + count_with_max(n, n-1)
    if d.has_key((n, max_term)): return d[(n, max_term)]
    result =  sum(count_with_max(n-i, i) for i in xrange(1, max_term+1))
    d[(n, max_term)] = result
    return result

def count(n):
    return count_with_max(n, n-1)
    
for i in xrange(1, 7):
    print i, count(i)

def problem76():
    return count(100)

print problem76()
