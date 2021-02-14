from itertools import count

flag = 0
t = int(input())
for i in range(t):
    s = input()
    for i in s:
        if i == s[0]:
            flag = 0
        else:
            flag = 1
            break
    if flag == 0:
        print(len(s))
    else:
        comb = []
        count1 = 0
        for i in range(len(s)):
            c1 = []
            for j in range(len(s), 0, -1):
                if j > i:
                    c1.append(s[i:j])

            comb.append(c1[::-1])

        ans = []
        for i in range(len(s)):
            for j in range(len(s)-i):
                if comb[j][i] in ans:
                    continue
                else:
                    if comb[j][i][::-1] in ans and comb[j][i].count('1') % 2 == 0:
                        continue
                    elif comb[j][i].count('1') % 2 == 0 and comb[j][i][::-1] == comb[j][i]:
                        ans.append(comb[j][i])
                    else:
                        ans.append(comb[j][i])
        print(len(ans))
