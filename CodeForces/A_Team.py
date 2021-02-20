c = 0
for _ in range(int(input())):
    arr = list(map(int, input().split(' ')))
    if arr.count(1) >= 2:
        c += 1
print(c)
