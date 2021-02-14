t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    p = list(input())
    # print(s, p)
    if s == p:
        print('Yes')
    else:
        for i in range(n):
            for j in range(i, n):
                if s[i] == '1' and s[j] == '0':
                    s[i] = '0'
                    s[j] = '1'
                    if s == p:
                        print("Yes")
                        break

                    else:
                        print("No")
