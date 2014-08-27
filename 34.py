
fact = {0:1, 1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}

def digits(n):
    if n < 10: return [n]
    return digits(n/10) + [n%10]

   
def sum_fact(n):
    return sum(map(lambda x: fact[x], digits(n)))
  
i = 1
total = 0
while i < 7*fact[9]:
    d = digits(i)
    if not (i%2 and not (0 in d or 1 in d)):
        if not reduce(lambda x,y: x or y, [d.count(di)*fact[di] >= i for di in d]):
            if i == sum_fact(i):
                print i
                total += i
    i += 1
   
print "result: ", total

