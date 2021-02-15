from itertools import combinations, count


def issame(lst):
    if len(lst) < 0:
        res = True
    res = lst.count(lst[0]) == len(lst)
    if res:
        return True
    else:
        return False


for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split(' ')))
    ans = set()
    if issame(ar):
        print(0)

    else:
        for i in range(len(ar)):
            for j in range(len(ar)):
                if i != j:
                    if ar[i] > ar[j]:
                        ans.add((i, ar[i]))
                    elif ar[i] < ar[j]:
                        ans.add((j, ar[j]))
                    else:
                        continue

        print(len(ans))
