n = int(input())
arr = list(map(int, input().split(',')))
val = sum(arr)/len(arr)
c = []
for i in arr:
    if(i-val) > 0:
        c.append(i-val)
print(int(sum(c)))
