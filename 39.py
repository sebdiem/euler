import time
import math

start = time.time()

squares = [i*i for i in xrange(1,1500)]
perimeters = {}
max_p = 1000

#hypothenus > a => a <= 499
for a in xrange(1,max_p/2):
    # 293 = 1000/(2+sqrt(2)) b ne peut etre plus grand que ca sinon le perimetre
    # est plus grand que 1000
    for b in xrange(1, min(293, a+1)):
        sq_sum = a**2 + b**2
        if sq_sum in squares:
            p = a + b + int(math.sqrt(sq_sum))
            if p <= max_p:
                if not perimeters.has_key(p): perimeters[p] = 1
                else: perimeters[p] += 1

print max(perimeters.items(), key=lambda x:x[1])
print "time: ", time.time() - start
