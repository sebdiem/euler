memo = {}
def fib(n):
    if n == 1: return 1
    if n == 2: return 1
    if memo.has_key(n):
        return memo[n]
    result = fib(n-1)+fib(n-2)
    memo[n] = result
    return result

def digit1000(minus1, minus2,i):
    fibo = minus1 + minus2
    j = i
    while len(str(fibo)) != 1000:
        minus2 = minus1
        minus1 = fibo
        fibo = minus1 + minus2
        j+=1
    return fibo,j
    
    
print digit1000(144,89,13)