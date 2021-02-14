# CodeBy Suyesh
def distinct(l1, l2):
    s = len(set(l1+l2))
    return s


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        l = input().split()
        b = {}
        for i in l:
            p = i[1:]
            if p in b:
                b[p].append(i[0])
            else:
                b[p] = [i[0]]
        body1 = list(b.keys())
        ans = 0
        for i in range(len(b)):
            for j in range(i+1, len(b)):
                temp = distinct(b[body1[i]], b[body1[j]])
                ans += (temp-len(b[body1[i]]))*(temp-len(b[body1[j]]))
        print(2*ans)
