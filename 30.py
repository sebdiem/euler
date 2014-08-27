
import itertools


def digits(n):
    if n < 10: return [n]
    return digits(n/10) + [n%10]

i = 2
result = []
while i < 6*9**5:
    d = digits(i)
    if i == sum([di**5 for di in d]):
        print i
        result.append(i)
    i += 1

print result, sum(result)
