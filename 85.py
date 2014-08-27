def count(lines, columns):
    return (columns*(columns+1))/2*(lines*(lines+1))/2

assert count(2, 3) == 18
print count(1, 2000)
print count(36, 77)

def problem85(N=2000000):
    return min(((abs(count(m, n) - N), (m,n)) for n in range(1, 1000) for m in range(1, n)))

lines, columns = problem85()[1]
print lines, columns, ' -> solution = ', lines*columns
    
