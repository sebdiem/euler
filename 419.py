SOURCE = """1	H	H  22	22
2	He	Hf Pa H Ca Li	13112221133211322112211213322112	11132132212312211322212221121123222112
3	Li	He	312211322212221121123222112	13112221133211322112211213322112
4	Be	Ge Ca Li	111312211312113221133211322112211213322112	3113112221131112211322212312211322212221121123222112
5	B	Be	1321132122211322212221121123222112	111312211312113221133211322112211213322112
6	C	B	3113112211322112211213322112	1321132122211322212221121123222112
7	N	C	111312212221121123222112	3113112211322112211213322112
8	O	N	132112211213322112	132112211213322112
9	F	O	31121123222112	132112211213322112
10	Ne	F	111213322112	31121123222112
11	Na	Ne	123222112	111213322112
12	Mg	Pm Na	3113322112	132123222112
13	Al	Mg	1113222112	3113322112
14	Si	Al	1322112	1113222112
15	P	Ho Si	311311222112	13211321322112
16	S	P	1113122112	311311222112
17	Cl	S	132112	1113122112
18	Ar	Cl	3112	132112
19	K	Ar	1112	3112
20	Ca	K	12	1112
21	Sc	Ho Pa H Ca Co	3113112221133112	132113213221232112
22	Ti	Sc	11131221131112	3113112221133112
23	V	Ti	13211312	11131221131112
24	Cr	V	31132	13211312
25	Mn	Cr Si	111311222112	311321322112
26	Fe	Mn	13122112	111311222112
27	Co	Fe	32112	13122112
28	Ni	Zn Co	11133112	31232112
29	Cu	Ni	131112	11133112
30	Zn	Cu	312	131112
31	Ga	Eu Ca Ac H Ca Zn	13221133122211332	11132221231132212312
32	Ge	Ho Ga	31131122211311122113222	132113213221133122211332
33	As	Ge Na	11131221131211322113322112	31131122211311122113222123222112
34	Se	As	13211321222113222112	11131221131211322113322112
35	Br	Se	3113112211322112	13211321222113222112
36	Kr	Br	11131221222112	3113112211322112
37	Rb	Kr	1321122112	11131221222112
38	Sr	Rb	3112112	1321122112
39	Y	Sr U	1112133	31121123
40	Zr	Y H Ca Tc	12322211331222113112211	11121332212311322113212221
41	Nb	Er Zr	1113122113322113111221131221	31131122212322211331222113112211
42	Mo	Nb	13211322211312113211	1113122113322113111221131221
43	Tc	Mo	311322113212221	13211322211312113211
44	Ru	Eu Ca Tc	132211331222113112211	111322212311322113212221
45	Rh	Ho Ru	311311222113111221131221	1321132132211331222113112211
46	Pd	Rh	111312211312113211	311311222113111221131221
47	Ag	Pd	132113212221	111312211312113211
48	Cd	Ag	3113112211	132113212221
49	In	Cd	11131221	3113112211
50	Sn	In	13211	11131221
51	Sb	Pm Sn	3112221	13213211
52	Te	Eu Ca Sb	1322113312211	1113222123112221
53	I	Ho Te	311311222113111221	13211321322113312211
54	Xe	I	11131221131211	311311222113111221
55	Cs	Xe	13211321	11131221131211
56	Ba	Cs	311311	13211321
57	La	Ba	11131	311311
58	Ce	La H Ca Co	1321133112	11131221232112
59	Pr	Ce	31131112	1321133112
60	Nd	Pr	111312	31131112
61	Pm	Nd	132	111312
62	Sm	Pm Ca Zn	311332	13212312
63	Eu	Sm	1113222	311332
64	Gd	Eu Ca Co	13221133112	11132221232112
65	Tb	Ho Gd	3113112221131112	132113213221133112
66	Dy	Tb	111312211312	3113112221131112
67	Ho	Dy	1321132	111312211312
68	Er	Ho Pm	311311222	1321132132
69	Tm	Er Ca Co	11131221133112	3113112221232112
70	Yb	Tm	1321131112	11131221133112
71	Lu	Yb	311312	1321131112
72	Hf	Lu	11132	311312
73	Ta	Hf Pa H Ca W	13112221133211322112211213322113	11132132212312211322212221121123222113
74	W	Ta	312211322212221121123222113	13112221133211322112211213322113
75	Re	Ge Ca W	111312211312113221133211322112211213322113	3113112221131112211322212312211322212221121123222113
76	Os	Re	1321132122211322212221121123222113	111312211312113221133211322112211213322113
77	Ir	Os	3113112211322112211213322113	1321132122211322212221121123222113
78	Pt	Ir	111312212221121123222113	3113112211322112211213322113
79	Au	Pt	132112211213322113	111312212221121123222113
80	Hg	Au	31121123222113	132112211213322113
81	Tl	Hg	111213322113	31121123222113
82	Pb	Tl	123222113	111213322113
83	Bi	Pm Pb	3113322113	132123222113
84	Po	Bi	1113222113	3113322113
85	At	Po	1322113	1113222113
86	Rn	Ho At	311311222113	13211321322113
87	Fr	Rn	1113122113	311311222113
88	Ra	Fr	132113	1113122113
89	Ac	Ra	3113	132113
90	Th	Ac	1113	3113
91	Pa	Th	13	1113
92	U	Pa	3	13""".split("\n")

import re
RE = "[0-9]+\s+(([a-zA-Z]+\s+)+)([0-9]+)"

ELEMENTS_NAME = [s.split()[1] for s in SOURCE]
ELEMENTS = [re.findall(RE, s)[0][2] for s in SOURCE]
EVOLUTION = [re.findall(RE, s)[0][0].split()[1:] for s in SOURCE]
EVOLUTION = [map(lambda x: ELEMENTS_NAME.index(x), t) for t in EVOLUTION]

def look_and_say(n):
    def next(l):
        i, last, count = 1, l[0], 1
        result = []
        while i < len(l):
            if l[i] != last:
                result += [count, last]
                last, count = l[i], 0
            i += 1
            count += 1
        result += count, last
        return result
    l = [1]    
    for i in range(n-1):
        l = next(l)
    return l

A,B,C = 0, 0, 0
for i in range(1, 8):
    l = look_and_say(i)
    A += l.count(1)
    B += l.count(2)
    C += l.count(3)
start1, start2 = 11132, 13211
A += 6
B += 2
C += 2
for i in range(9, 41):

print "".join([str(x) for x in look_and_say(8)]) in ELEMENTS

