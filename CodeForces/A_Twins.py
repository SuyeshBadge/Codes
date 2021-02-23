n = int(input())
arr = list(map(int, input().split(' ')))
# arr = [4,2,2,2,2]
arr.sort(reverse=True)
ans = []
for i in arr:
    if sum(ans) <= (sum(arr)-sum(ans)):
        ans.append(i)
    else:
        break
print(len(ans))
