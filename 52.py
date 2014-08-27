def problem52():
    k = 1
    while True:
        l = [tuple(sorted(str(i*k))) for i in xrange(2,7)]
        if l.count(l[0]) == 5: return k
        k += 1

print problem52()
