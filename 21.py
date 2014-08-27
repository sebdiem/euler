
def sum_of_dividers(n):
    if n == 1: return 0
    upper_bound = (n+1)/2 + 1
    i = 2
    result = 1
    while i < upper_bound:
        if not n%i:
            result += i + n/i
            upper_bound = n/i
        i += 1
    return result

N = 10**4

def problem21():
    result = 0
    l = []
    explore = range(2, N+1)
    j = 0
    while j < len(explore):
        i = explore[j]
        s1 = sum_of_dividers(i)
        print i, s1
        if s1 != i:
            s2 = sum_of_dividers(s1)
            if s2 == i:
                result += i + s1
                l.append((i,s1))
                if s1 < N+1:
                    if s1 in explore:
                        explore.remove(s1)
        j += 1
    return result, l
   
print problem21()
           

