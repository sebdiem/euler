attempts = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716""".split()

def add_wo_doubles(list1, list2):
    add = []
    for e in list2:
        if not e in list1: add.append(e)
    return list1 + add

constraints = {}

for a in attempts:
    i1,i2,i3 = [c for c in a]
    if not constraints.has_key(i1): constraints[i1] = []
    constraints[i1]= add_wo_doubles(constraints[i1], [i2,i3])
    if not constraints.has_key(i2): constraints[i2] = []
    constraints[i2] = add_wo_doubles(constraints[i2], [i3])

constraints = constraints.items()
constraints = sorted(constraints, key=lambda x: len(x[1]))
print constraints
result = []
for i, lc in constraints:
    for c in lc:
        if c not in result: result = [c] + result
    if i in result: print "problem: " + i
    else: result = [i] + result
print reduce(lambda x,y: x+y, result)
    
    

