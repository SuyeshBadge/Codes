# CodeBy Suyesh Badge
import sys
import io
import os


def soe(k):
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
        count_p.append(c)
    return(count_p[k])


if __name__ == "__main__":
    count_p = []
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n = input().decode()
    soe()
    for _ in range(int(n)):
        x, y = map(int, input().decode().split(' '))
        l = count_p[x]
        if l <= y:
            sys.stdout.write("Chef\n")
        else:
            sys.stdout.write("Divyam\n")
