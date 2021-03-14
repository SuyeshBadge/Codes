import math


def mex(arr):
    lst = list(i for i in range(max(arr)))
    for i in lst:
        if i not in arr:
            return i


for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    a = mex(arr)
    b = max(arr)
    if a is None:
        print(len(set(arr))+k)
    else:
        for i in range(k):
            if a is not None:
                arr.append(math.ceil((a+b)/2))

        print(len(set(arr)))
