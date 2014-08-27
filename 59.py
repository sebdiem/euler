# Recall that python XOR operator is ^
# For example 65 ^ 42 = 107

CHAR = 'abcdefghijklmnopqrstuvwxyz'

FREQ = {
    'a':   8.167/100,  
    'b':  1.492/100,  
    'c': 2.782/100,  
    'd':    4.253/100,  
    'e':   12.702/100, 
    'f':  2.228/100,  
    'g': 2.015/100,  
    'h':    6.094/100,  
    'i':   6.966/100,  
    'j':  0.153/100,  
    'k': 0.772/100,  
    'l':    4.025/100,  
    'm':   2.406/100,  
    'n':  6.749/100,  
    'o': 7.507/100,  
    'p':    1.929/100,  
    'q':   0.095/100,  
    'r':  5.987/100,  
    's': 6.327/100,  
    't':    9.056/100,  
    'u':   2.758/100,  
    'v':  0.978/100,  
    'w': 2.360/100,  
    'x':    0.150/100,  
    'y':   1.974/100,  
    'z':  0.074/100,
}

def test(key, text):
    freq = dict([(c, 0) for c in FREQ.keys()])
    for i, code in enumerate(text):
        decrypt = chr(int(code) ^ ord(key[i%len(key)]))
        if decrypt in freq.keys():
            freq[decrypt] += 1
    freq = dict([(c, 1.*i/len(text)) for c, i in freq.items()])
    return sum([(FREQ[k] - freq[k])**2 for k in FREQ.keys()])


def problem59():
    f = open('cipher1.txt')
    text = f.read().replace('\n', '').split(',')
    import itertools
    candidates = itertools.product(FREQ.keys(), repeat=3)
    key = min(candidates, key=lambda x:test(x, text))
    decipher = [chr(ord(key[i%len(key)]) ^ int(text[i])) for i in range(len(text))]
    print 'Key: %s' % str(key)
    print ''.join(decipher)
    return sum([ord(c) for c in decipher])

print problem59()


