import time

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.reverse()

start = time.time()

def sum_coins(n):
    if n == 0: raise
    result = 0
    stack = []
    i = 0
    j = 0
    while coins[i] > n:
        i += 1
    stack.append(coins[i])
    while not len(stack) or stack[0] != 1:
        current = sum(stack)
        if current == n:
            result += 1
            if not stack: i += 1    
            else: i = coins.index(stack[j]) + 1
            stack = stack[:j]
            j -= 1
        else:
            while coins[i] + current > n:
                i += 1
            stack.append(coins[i])
            if coins[i] > 1: j += 1
    return result + 1 # le dernier resultat avec que des 1 n'a pas ete compte

"""
print "result: ", sum_coins(200)
"""

memo = {}

def rec_sum(total, max_coin):
    if memo.has_key((total, max_coin)): return memo[(total, max_coin)]
    if total == 0 or max_coin == len(coins) - 1: return 1
    result, i = 0, 0
    next_coin = coins[max_coin]
    while i*next_coin <= total:
        result += rec_sum(total - i*next_coin, max_coin + 1)
        i += 1
    memo[(total, max_coin)] = result    
    return result

print rec_sum(1000, 0)
print "time: ", time.time() - start
