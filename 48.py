s = sum([i**i for i in range(1,1001)])
r = []
for k in range(1,11):
    r.append(s%10)
    s /= 10
r.reverse()
print "".join(map(lambda x: str(x), r))
