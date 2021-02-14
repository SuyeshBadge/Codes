from collections import Counter
for _ in range(int(input())):
    t = int(input())
    bb = list(map(int, input().split()))
    i = 0
    c = 1
    f = list(Counter(bb).values())
    print(max(f))
