import math
t = int(input())

for _ in range(t):
    N, X = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    i = 0
    k = X
#
    while k > 0 and i < N-1:
        flag = 0
        p = int((math.log(arr[i])/(math.log(2))))
        r = int(1 << p)
        arr[i] = arr[i] ^ r
        j = i+1
        while j < N:
            if (arr[j] ^ r) < arr[j]:
                arr[j] = arr[j] ^ r
                flag = 1
                break
            j += 1
        if flag == 0:
            arr[N-1] = arr[N-1] ^ r
        while arr[i] <= 0:
            i += 1
        z = k+1
        k = k-1
    if z > 0:
        if (N < 3) and (z % 2 > 0):
            arr[N-1] = arr[N-1] ^ 1
            arr[N-2] = arr[N-2] ^ 1

    for i in arr:
        print(i, end=' ')
