n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

c = 0
flg = arr[k-1]
if sum(arr) > 0:
    for i in arr:
        if i >= flg and i > 0:
            c += 1
print(c)
