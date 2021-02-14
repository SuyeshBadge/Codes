from itertools import permutations


def split(word):
    return [char for char in word]


for _ in range(int(input())):
    n = int(input())
    b = int(input())
    s = '1'*n+'0'*n
    a = list(set(permutations(s, n)))
    ans = 0
    d1 = {}
    for j in a:
        temp = int(''.join(j))
        d = split(str(int(b)+temp))
        f = 0
        while f < len(d)-1:
            if d[f] == d[f+1]:
                d.pop(f)
            f += 1
        d2 = int(''.join(d))

        d1[d2] = temp
    ans = max(d1)
    print(d1[ans])
