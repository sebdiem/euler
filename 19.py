days = ["S","M","T","W","t","F","s"]

def count_days(year):
    if not year%100 and year%400: return 365
    if year%4: return 365
    return 366

def months(year):
    feb = 28 if count_days(year) == 365 else 29
    return [("J",31), ("F",feb), ("M",31), ("A",30) , ("m",31) , ("J",30),
            ("j",31), ("a",31), ("S",30), ("O",31), ("N",30), ("D",31)]

print count_days(2000)
print count_days(1900)
print count_days(1986)
print count_days(1999)%7

start = 1 # 1st january 1900 is monday (M) : index 1
start += count_days(1900)%7 # index of 1st day of 1901
print "start: ", start
year = 1901
month = 0
count_sundays = 0
while year < 2001:
    m = months(year)
    if days[start] == "S":
        count_sundays += 1
        print m[month][0], year
    start = (start + m[month][1])%7
    month = (month + 1)%12
    if month == 0:
        year += 1

print "count: " , count_sundays
