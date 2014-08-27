import itertools

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome(n):
    result = 0
    for i,j in itertools.combinations(range(10**(n-1), 10**n), 2):
        product = i*j
        if product > result and is_palindrome(product):
            result = product
    return result

print largest_palindrome(3)
