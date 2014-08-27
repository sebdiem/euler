def triangle(n):
    return (n*(n+1))/2

def square(n):
    return n*n

def pentagonal(n):
    return (n*(3*n-1))/2

def hexagonal(n):
    return n*(2*n-1)

def heptagonal(n):
    return (n*(5*n-3))/2

def octagonal(n):
    return n*(3*n-2)

def problem61():
    numbers_collection, prefixes, suffixes = build_collections()
    candidates = ([], [], [], [], [], [])
    # start with last function_id=4 because it contains less prefixes
    start_id = 4
    candidate_chains = [[(prefix, suffix, [start_id])]
                         for prefix, suffixes in prefixes[start_id].items()
                         for suffix in suffixes]
    while candidate_chains:
        current_chain = candidate_chains.pop()
        if len(current_chain) < 6:
            current_prefix, current_suffix, current_function_id = current_chain[-1]
            successors = find_successors(current_prefix, current_suffix, current_function_id,
                                         prefixes, suffixes)
            if successors: candidate_chains.extend([current_chain + [s] for s in successors])
        else:
            if current_chain[-1][1] == current_chain[0][0]:
                print sum((int(c[0]+c[1]) for c in current_chain))

def build_collections():
    numbers_collection = ([], [], [], [], [], [])
    functions = (triangle, square, pentagonal, hexagonal, heptagonal, octagonal)
    prefixes = (dict(), dict(), dict(), dict(), dict(), dict())
    suffixes = (dict(), dict(), dict(), dict(), dict(), dict())
    n_max_4_digits = 150
    for n in xrange(n_max_4_digits):
        for i, f in enumerate(functions):
            candidate = f(n)
            if 999 < candidate < 10000:
                numbers_collection[i].append(candidate)
                candidate_string = str(candidate)
                assert len(candidate_string) == 4
                prefix, suffix = candidate_string[:2], candidate_string[2:] 
                dicts_keys = ((0, prefixes[i], prefix), (1, suffixes[i], suffix))
                for j, d, key in dicts_keys:
                    if d.has_key(key):
                        d[key].append(dicts_keys[1-j][2])
                    else: d[key] = [dicts_keys[1-j][2]]
    return numbers_collection, prefixes, suffixes

def find_successors(prefix, suffix, function_ids, prefixes, suffixes):
    successors = []
    for i in xrange(6):
        if not i in function_ids and suffix in prefixes[i].keys():
            successors.extend([(suffix, s, function_ids + [i])
                               for s in prefixes[i][suffix]])
    return successors

N_COL, PREF, SUF = build_collections()
tr = 100*101/2
assert str(tr)[:2] in PREF[0].keys()
assert str(tr)[2:] in SUF[0].keys()


problem61()

