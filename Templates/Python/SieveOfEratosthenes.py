def soe(k):
    count_p = []
    allprime = []
    n = 1000002
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
            allprime.append(i)
        count_p.append(c)
    return(count_p[k], allprime[:count_p[k]])


print(soe(1000))
