def is_palindrome(n):
    s = str(n)
    for i in range(len(s)/2):
        if s[i] != s[len(s)-i-1]: return False
    return True
"""   
print is_palindrome(12345)
print is_palindrome(13231)
print is_palindrome(1)
print is_palindrome(134431)
print is_palindrome(132431)
"""

def is_lychrel(n):
    current, i = n, 0
    while i < 50:
        s = str(current)
        current += int(s[::-1])
        if is_palindrome(current): return False
        i += 1
    return True
   
def problem55():
    return sum((is_lychrel(n) for n in xrange(10**4)))
   
print problem55()


