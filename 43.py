"""
d4 est divisible par 2 : 0,2,4,6,8
d3+d4+d5 est divisible par 3
d6 est 5 ou 0  
d6 + d8 = d7
"""
import itertools

def calculate(n_list):
    l = len(n_list)
    return sum([k*10**(l-i-1) for i,k in enumerate(n_list)])

def special_pandigital():
    pandigitals = itertools.permutations(range(10), 10)
    result = 0
    for p in pandigitals:
        """
        if not calculate(p[1:4]) % 2 and not calculate(p[2:5]) % 3 and \
           not calculate(p[3:6]) % 5 and not calculate(p[4:7]) % 7 and \
           not calculate(p[5:8]) % 11 and not calculate(p[6:9]) % 13 and \
           not calculate(p[7:]) % 17:
            c = calculate(p)
            print c
            result += c"""
        if p[0] != 0:
            if (p[5] == 0 or p[5] == 5):
                if not p[3] % 2:
                    if not sum(p[2:5]) % 3:
                        if not calculate(p[5:8]) % 11:
                            if not calculate(p[4:7]) % 7:
                                if not calculate(p[6:9]) % 13:
                                    if not calculate(p[7:]) % 17:
                                        c = calculate(p)
                                        print c
                                        result += c
    return result
                        
                
print special_pandigital()
    
