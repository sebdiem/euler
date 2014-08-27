def cycle_length(n):
    r = 1
    remains = []
    while r not in remains:
        remains.append(r)
        r = (r*10)%n
    return len(remains) - remains.index(r)

print cycle_length(6)
print cycle_length(7)
print cycle_length(8)
print cycle_length(13)

best_length = 0
best = 0
i = 1
while i < 1000:
    c = cycle_length(i)
    if c > best_length:
        best_length = c
        best = i
    i += 1
print best, best_length
