# Persistent


def div1(n1, n2, s):
    while n1 >= 1:
        s += str(n1 % n2)
        n1 = n1//n2
    else:
        return s[::-1]


for _ in range(int(input())):
    n = int(input())
    s = ""
    c = 0
    if n == 1:
        print("infinity")
        continue
    for i in range(2, n+1):
        s1 = div1(n, i, s)
        if s1[0] == '1':
            c += 1
    print(c)
