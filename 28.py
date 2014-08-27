l = lambda n: 2*n+1 # length of the side of the 'square' of distance n to the center
edge = lambda n: 4*n*(n+1) + 1
# 1001x1001 corresponds to the square of distance 500

result = 1 # center is 1
for i in range(1, 501):
    result += edge(i)
    result += edge(i) - (l(i) - 1)
    result += edge(i) - 2*(l(i) - 1)
    result += edge(i) - 3*(l(i) - 1)
print result
