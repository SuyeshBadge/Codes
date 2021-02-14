t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split(' ')))
    c = []
    if n == 1:
        print(1)
    elif all(i == x[0] for i in x):
        print(2)

    else:
        for i in range(n-1):
            if x[i] == x[i+1]:
                x[i] += 1
        if x[-1] == x[-3]:
            x[-1] += 1
        print(len(set(x)))
