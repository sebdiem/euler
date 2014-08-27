for b in range(501):    
    for a in range(334):
        c = (a**2 + b**2)**0.5
        if c == int(c) and a + b + c == 1000:
            print a*b*c
