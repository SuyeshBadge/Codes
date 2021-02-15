
for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    a = n
    b = 1
    i = 1
    flag = True
    while i < k:
        if a == b:
            if b < n:
                b += 1
            else:
                b = 1
        if a == 1:
            a = n
        else:
            a -= 1
        if b == n:
            b = 1
        else:
            b += 1
        i += 1
        if a == b:
            if b < n:
                b += 1
            else:
                b = 1
    print(b)
