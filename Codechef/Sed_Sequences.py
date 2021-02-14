

t = int(input())
for _ in range(t):
    n, k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    cnt = 0
    if sum(arr) % k == 0:
        print(cnt)
    else:
        print(1)
