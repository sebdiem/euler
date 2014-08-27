def is_candidate(n):
    s = str(n)
    return reduce(lambda x,y: x and y,[s.count(c) == 1 for c in s])

def is_pandigital(n):
    s = str(n)
    if "0" in s: return False
    return reduce(lambda x,y: x and y,[s.count(c) == 1 for c in "123456789"])

d = {0:0,1:9,2:4,3:9,4:4,5:1,6:4,7:9,8:4,9:9}

print is_pandigital(123456789)

pan_max = 0
for i in range(1, 10**5):
    if is_candidate(i):
        u = int(str(i)[-1])
        pan = i
        for k in range(2, d[u]+1):
            pan = int(str(pan)+str(k*i))
            if not is_candidate(pan): break
            if is_pandigital(pan):
                print "new pan:", i, pan
                if pan > pan_max:
                    pan_max = pan
                    print "new max:", i, pan
                break
    
        
