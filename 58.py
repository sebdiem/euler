def is_prime(n):
    if n == 0 or n == 1: return False
    if n == 2 or n == 3 or n == 5: return True
    i = 2
    while i <= n**0.5:
        if not n%i: return False
        i += 1
    return True

assert is_prime(7)
assert is_prime(11)
assert is_prime(13)
assert is_prime(17)
assert is_prime(19)
assert not is_prime(6)
assert not is_prime(8)
assert not is_prime(9)
assert not is_prime(10)

def diagonals():
    i0 = 3
    square_length = 3
    while True:
        yield i0, i0+square_length-1, i0+2*(square_length-1), i0+3*(square_length-1)
        i0 = i0+3*(square_length-1)+square_length+1
        square_length += 2

diagonal_gen = diagonals()

def problem58(threshold=0.1):
    square_length = 3
    total_diag = 5
    primes = 3
    diagonal_gen.next()
    while 1.*primes/total_diag > threshold:
        square_length += 2
        total_diag += 4
        primes += sum([is_prime(i) for i in diagonal_gen.next()])
    return square_length

print problem58()

