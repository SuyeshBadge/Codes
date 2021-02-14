def inttime(p):
    p1 = p[0].split(':')
    if "AM" in p and p1[0] == '12':
        p = int("".join(p1))-1200
    elif "PM" in p and p1[0] == '12':
        p = int("".join(p1))
    elif "PM" in p and p1[0] != '12':
        p = int("".join(p1))+1200
    elif "AM" in p and p1[0] != '12':
        p = int("".join(p1))
    return p


for _ in range(int(input())):
    p = input().split(' ')
    pp = inttime(p)
    n = int(input())
    for i in range(n):
        f = input().split(' ')
        t1 = inttime(list(f[0:2]))
        t2 = inttime(list(f[2:4]))
        if pp >= t1 and pp <= t2:
            print('1', end='')
        else:
            print('0', end='')
    print()
