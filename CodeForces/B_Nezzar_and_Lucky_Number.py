def check(n, d):
    if n < d:
        print("NO")
        return 0
    elif (n-d) % 10 == d:
        print("YES")
        return True
    else:
        check(n-d, d)


for _ in range(int(input())):
    q, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        if i % 10 == d:
            print("YES")
        else:
            check(i, d)
