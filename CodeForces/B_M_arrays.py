from itertools import combinations
for _ in range(int(input())):
    n, m = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    arr.sort()
    comb = list(combinations(arr, 2))
    print(comb)
    p = []
    for i in comb:
        if sum(i) % m == 0:
            pass
