import functools
from math import ceil, floor

global PRIMES


PRIMES = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367,
373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821,
823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
983, 991, 997 }


def could_be_square(x):
    # 0 => 0
    # 1 => 1
    # 2 => 4
    # 3 => 9
    # 4 => 6
    # 5 => 5
    # 6 => 6
    # 7 => 9
    # 8 => 4
    # 9 => 1
    return str(x)[-1] not in {2, 3, 7, 8}


@functools.lru_cache(maxsize=None)
def is_square(x):
    if not could_be_square(x): return False
    return int(x ** 0.5) ** 2 == x


def minimal_x(D):
    """Find the minimal x solution of x**2 - D*y**2 = 1 for a given D.
       If D is prime, y ** 2 is of the form:
          y ** 2 = p * (D * p + 2)
          or
          y ** 2 = p * (D * p - 2)
    """
    assert not is_square(D)
    D_unit = int(str(D)[-1])
    y_unit = 1
    if D in PRIMES:
        for p in range(1, 10 ** 8):
            Dp2 = D * p * p
            two_p = 2 * p
            y2_candidates = (Dp2 + two_p, Dp2 - two_p)
            for c in y2_candidates:
                if is_square(c):
                    return int((1 + D * c) ** 0.5)
    else:
        for y in range(1, 2 * 10 ** 8):
            y_unit = (y_unit + 1) % 10
            if could_be_square(1 + D_unit * (y_unit ** 2)):
                if is_square(1 + D * (y ** 2)):
                    return int((1 + D * (y ** 2)) ** 0.5)
    print('not found')



def bhaskara(D):
    """Actually clever people managed to compute this way faster without computers oO.
       See: https://fr.wikipedia.org/wiki/M%C3%A9thode_chakravala
    """
    a = 1
    b = 0
    N = a ** 2 - D * b **2
    while b == 0 or abs(N) not in (1, 2, 4):
        m = min(
            (abs(x ** 2 - D), x)
            for x in range(1, D)
            if ((b * x) % N) == (-a % N)
        )[1]

        a, b = (a * m + D * b) // abs(N), (a + m * b) // abs(N)
        N = a ** 2 - D * b **2

    if N == 1:
        return (a, b)
    if N == -1:
        return (a ** 2 + D * (b ** 2), 2 * a * b)
    if abs(N) == 2:
        return ((a ** 2 + D * (b ** 2)) // 2, a * b)
    # abs(N) == 4
    epsilon = N / abs(N)
    if a % 2 == 0 and b % 2 == 0:
        if epsilon == 1:
            return (a // 2, b // 2)
        else:
            return ((a ** 2 + D * (b ** 2)) // 4, a * b // 2)
    if D % 2 == 0:
        return ((a ** 2 + D * (b ** 2)) // 4, a * b // 2)
    if epsilon == 1:
        return ((a ** 3 + 3 * a * b ** 2 * D) // 8, (D * b ** 3 + 3 * a ** 2 * b) // 8)
    return ((a ** 6 + 15 * a ** 4 * b ** 2 * D + 15 * a ** 2 * b ** 4 * D ** 2 + b ** 6 * D ** 3) // 64, (6 * a ** 5 * b + 20 * a ** 3 * b ** 3 * D + 6 * a * b ** 5 * D ** 2) // 64)


assert bhaskara(2)[0] == 3
assert bhaskara(61)[0] == 1766319049
assert bhaskara(103)[0] == 227528
assert bhaskara(3)[0] == 2
assert bhaskara(5)[0] == 9
assert bhaskara(6)[0] == 5
assert bhaskara(7)[0] == 8
assert bhaskara(20)[0] == minimal_x(20)
assert bhaskara(21)[0] == minimal_x(21)

for x in range(22, 61):
    if not is_square(x):
        assert bhaskara(x)[0] == minimal_x(x)

def problem_66():
    return max((bhaskara(D), D) for D in range(2, 1001) if not is_square(D))[1]

if __name__ == '__main__':
    print(problem_66())
