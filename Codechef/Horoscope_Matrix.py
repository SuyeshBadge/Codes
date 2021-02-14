t = int(input())
for _ in range(t):
    n, m = map(int, input().split(' '))
    arr = []
    for __ in range(n):
        l1 = list(map(int, input().split(' ')))
        arr.append(l1)
    q = int(input())
    for i in range(q):
        x, y, v = map(int, input().split(' '))
        arr[x-1][y-1] = v
        for _1 in range(n-1):
            if arr[_1][_1] != arr[_1+1][_1+1]:
                print("No")
            else:
                print("Yes")
