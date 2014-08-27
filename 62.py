def problem62():
    n = 20
    cubes_digits_ordered = dict()
    while True and  n < 10000:
        latest = ''.join(sorted(str(n**3)))
        if cubes_digits_ordered.has_key(latest):
            cubes_digits_ordered[latest].append(n**3)
        else: cubes_digits_ordered[latest] = [n**3]
        if len(cubes_digits_ordered[latest]) == 5:
            return cubes_digits_ordered[latest][0]
            break
        n += 1

print problem62()
