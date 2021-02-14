import math
from collections import Counter


def crar(n, k):
    a = []
    for i in range(n):
        a.append(1)
    if sum(a) % k == 0:
        return a
    else:
        i = 0
        while sum(a) % k != 0:
            if i >= n-1:
                i = 0

            a[i] += 1
            i += 1
        else:
            return a


for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    ar = crar(n, k)
    ch = Counter(ar)
