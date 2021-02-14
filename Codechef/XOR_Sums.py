n = int(input())
arr = list(map(int, input().split(' ')))

for _ in range(int(input())):
    res = 0
    m = int(input())
    if m > 1:
        for i in range(n):
            for j in range(i, n):
                res += arr[i] ^ arr[j]
        print(sum(arr)+res)
    else:
        print(sum(arr))
