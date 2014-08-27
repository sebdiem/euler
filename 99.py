from numpy import log

f  = open('base_exp.txt')
BASE_EXP = [(int(s.split(',')[0]), int(s.split(',')[1])) for s in f.read().split()]
f.close()
print [log(b)*e for b,e in BASE_EXP[:10]]

print max(((log(b_e[0])*b_e[1], i+1) for i, b_e in enumerate(BASE_EXP)))
