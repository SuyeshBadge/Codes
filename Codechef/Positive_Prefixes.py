t = int(input())
for i in range(t):
    n, k = map(int, input().split(' '))
    if (k == n):
        for j in range(1, n+1):
            print(j, end=' ')
    elif(k < n):
        if n % 2 == 0:
            div = n/2
        else:
            div = (n//2)+1
        if (k >= div):
            k = n-k
            for i in range(1, n+1):
                if i % 2 == 0:
                    if k > 0:
                        print(i * -1)
                        k -= 1
                    else:
                        print(i)
                else:
                    print(i)
        else:
            for i in range(1, n+1):
                if i % 2 != 0:
                    if k > 0:
                        print(i)
                        k -= 1
                    else:
                        print(i*-1)
                else:
                    print(i*-1)
