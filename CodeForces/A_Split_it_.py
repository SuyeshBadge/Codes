for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    s = input()
    t = n-k+1
    temp = s[1:k]+s[t:n]
    if k == 0 or temp == temp[::-1]:
        if 2*k < n:
            print("YES")
        else:
            print('NO')
    else:
        print('NO')
