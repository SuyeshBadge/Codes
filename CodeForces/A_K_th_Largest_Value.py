n, q = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
for _ in range(q):
    t, x = map(int, input().split(' '))
    if t == 1:
        arr[x-1] = 1-arr[x-1]
    elif t == 2:
        arr.sort(reverse=True)
        print(arr[x-1])
