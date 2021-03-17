from collections import Counter


def mex(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] > i:
            return i


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    b = []
    if n > 1:
        cnt = Counter(arr)
        b = sorted(arr)

        for i, j in enumerate(b):
            if cnt[j] > 1:
                b.pop(i)
                b.append(j)

        for i in b:
            print(i, end=' ')
        print()
    else:
        print(0)
