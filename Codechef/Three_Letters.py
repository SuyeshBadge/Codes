t = int(input())
for _ in range(t):
    str1 = input()
    count1 = {}
    c = 0
    for i in str1:
        if i in count1:
            count1[i] += 1
        else:
            count1[i] = 1
    for i in count1:
        if count1[i] % 2 == 0:
            c += 1
    print(c)
