def soe(n):

    prime = [1 for i in range(n + 1)]
    p = 2

    while (p * p <= n):

        if (prime[p] == 1):
            for i in range(p * 2, n + 1, p):
                prime[i] = 0

        p += 1
    prime[0] = 0
    prime[1] = 0
    c = 0
    for i in range(n):
        if (prime[i]):
            c += 1
        count_p.append(i)


count_p = []
soe(100)
