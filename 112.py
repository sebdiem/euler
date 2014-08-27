def is_bouncy(n):
    if n < 10: return False
    s = str(n)
    direction = None # stores the first estimated direction: 'i' for incr, 'd' for decr
    for i in range(1, len(s)):
        if not direction:
            diff = int(s[i]) - int(s[0])
            if diff != 0: direction = ('i', 'd')[diff < 0]
        else:
            diff = int(s[i]) - int(s[i-1])
            if diff and ('i', 'd')[diff < 0] != direction: return True
    return False

print is_bouncy(155349)
print is_bouncy(12)
print is_bouncy(123456789)
print is_bouncy(987654321)
print is_bouncy(33333)
print is_bouncy(36321)
print is_bouncy(367891)
print is_bouncy(98769)
print is_bouncy(1000)
print is_bouncy(101)

def problem132(limit=0.99):
    i = 100
    count = 0
    while count < limit*(i-1):
        count = count+1 if is_bouncy(i) else count
        i += 1
    return i-1

print sum([is_bouncy(i) for i in range(1001)])
print problem132(0.5)
print problem132()
