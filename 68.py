from itertools import permutations
for a, b, c, d, e, f, g, h , i in permutations(xrange(1, 10)):
    aim = 10 + a + b
    if aim == c + b + d and aim == e + d + f and aim == g + f + h and aim == i + h + a:
       print ((10, a, b), (c, b, d), (e, d, f), (g, f, h), (i, h, a))
