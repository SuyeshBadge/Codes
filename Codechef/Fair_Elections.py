t = int(input())
for _ in range(t):
    n, m = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    a.sort()
    b.sort(reverse=True)
    c = 0
    for i in range(min(n, m)):
        if sum(a) < sum(b):
            temp = a[i]
            a[i] = b[i]
            b[i] = temp
            c += 1
        else:
            break

    print(c)
