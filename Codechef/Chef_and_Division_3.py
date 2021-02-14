t = int(input())
for _ in range(t):
    n, k, d = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    if sum(a) < k:
        print(0)
    else:
        if sum(a)//k > d:
            print(d)
        else:
            print(sum(a)//k)
