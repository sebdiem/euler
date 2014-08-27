number_dic = {1:"one",
              2:"two",
              3:"three",
              4:"four",
              5:"five",
              6:"six",
              7:"seven",
              8:"eight",
              9:"nine",
              10:"ten",
              11:"eleven",
              12:"twelve",
              13:"thirteen",
              14:"fourteen",
              15:"fifteen",
              16:"sixteen",
              17:"seventeen",
              18:"eighteen",
              19:"nineteen",
              20:"twenty",
              30:"thirty",
              40:"forty",
              50:"fifty",
              60:"sixty",
              70:"seventy",
              80:"eighty",
              90:"ninety",
              100:"hundred",
              1000:"thousand"}

def nearest_power_of_ten(n):
    # returns the power of ten just below or equal n
    k = 0
    while 10**k <= n:
        k += 1
    k -= 1
    return k

def decompose(n, k=-1):
    if k < 0: k = nearest_power_of_ten(n)
    n_list = []
    temp = n
    for i in range(k+1):
        n_list.append(int(temp/10**(k-i)))
        temp -= n_list[-1]*(10**(k-i))
    return n_list

def calculate(n_list):
    l = len(n_list)
    return sum([k*10**(l-i-1) for i,k in enumerate(n_list)])

def spell(n):
    if number_dic.has_key(n) and n < 100:
        return number_dic[n]
    n_list = decompose(n)
    if n < 100:
        return "%s %s" % (number_dic[n_list[0]*10], number_dic[n_list[1]])
    if n < 1000:
    # below 1000 > n > 100
        n_prime = calculate(n_list[1:])
        if n_prime > 0:
            return "%s %s %s %s" % (number_dic[n_list[0]], number_dic[100],
                                       "and", spell(n_prime))
        else:
            return "%s %s" % (number_dic[n_list[0]], number_dic[100])
    if n == 1000: return "one thousand"
    raise

result = 0        
for i in range(1,1001):
    result += len(spell(i).replace(" ",""))
print result
