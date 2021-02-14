for _ in range(int(input())):
    n = int(input())
    m = int(input())
    ar = list(map(int, input().split(' ')))
    ans = []
    for k in range(1, 8):
        if k == 1:
            mj = n-1
            sum = k+mj
            ans.append(sum)
        else:
            i = 0
            x = k
            c = 0
            while i < n:
                if i+x < n:
                    i += x
                    c += 1
                else:
                    i = n
                    c += 1
            sum = k+c
            ans.append(sum)
    print(min(ans))
