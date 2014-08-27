def is_palindrome(s):
    for i in range(len(s)/2+1):
        if s[i] != s[-(i+1)]: return False
    return True

print is_palindrome("boob")
print is_palindrome("booaoob")

def convert_base(n,i):
    if n < i: return str(n)
    return convert_base(n/i, i) + str(n%i)

print convert_base(585,2)
    

N = 10**6
result = 0
for i in xrange(N+1):
    if is_palindrome(str(i)):
        if is_palindrome(convert_base(i, 2)):
            result += i
print result
