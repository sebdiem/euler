# 1_2_3_4_5_6_7_8_9_0

for i in range(10 ** 9, 10 ** 10 + 1, 10):
    if str(i ** 2)[::2] == '1234567890':
        print(i)
