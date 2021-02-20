# arr = list(map(int, input().split(' ')))
arr = [0, 1, 2, 1, 1, 2, 1, 1, 0, 0, 1, 1, 2, 0]
zc = arr.count(0)
oc = arr.count(1)
tc = arr.count(2)
ans = []
for i in range(len(arr)):
    if i < zc:
        ans.insert(0, 0)
    elif i >= zc and i < oc+zc:
        ans.append(1)
    elif i >= oc and i < tc+oc+zc:
        ans.append(2)
print(ans)
