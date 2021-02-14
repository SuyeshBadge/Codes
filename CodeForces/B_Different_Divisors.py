def diff(a):
    l1 = []
    for i in range(len(a)-1):
        l1.append(a[i+1]-a[i])
    return l1


for _ in range(int(input())):
    d = int(input())
    n = 6
    while True:
        div = [1, n]
        for i in range(2, n):
            if n % i == 0:
                div.append(i)
        div.sort()
        l = diff(div)
        if min(l) >= d and len(div) >= 4:
            print(n)
            break
        else:
            n += 1
