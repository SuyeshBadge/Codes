import math
t = int(input())
for i in range(t):
    r = []
    nr = []
    n, d = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    for j in a:
        if j <= 9 and j >= 80:
            r.append(j)
        else:
            nr.append(j)
    days = 1
    r1 = len(r)
    nr1 = len(nr)
    while r1 > 0 or nr1 > 0:
        if r1 > 0:
            r1 -= d
            days += 1
        elif nr1 > 0:
            nr1 -= d
            days += 1
    print(days-1)
