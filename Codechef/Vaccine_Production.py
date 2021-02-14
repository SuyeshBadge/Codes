
d1, v1, d2, v2, p = map(int, input().split())
if d1 == d2:
    v = v1+v2
    while p > 0:
        p -= v
        d1 += 1
    print(d1-1)
else:
    i = 1
    while p > 0:
        if i >= d1:
            p -= v1
        if i >= d2:
            p -= v2
        i += 1
    print(i-1)
