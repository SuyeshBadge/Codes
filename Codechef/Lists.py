if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        ls = input().split(' ')
        cmd = ls[0]
        ls.pop(0)
        l = []
        for i in ls:
            l.append(int(i))
        if 'insert' in cmd:
            li[int(ls[0])] = int(ls[1])
        elif 'print' in cmd:
            print(li)
        elif 'remove' in cmd:
            for r, _ in enumerate(li):
                if len(l) > 0 and _ == l[1]:
                    li.pop(r)
                    break
        elif 'append' in cmd:
            for i in l:
                l.append(int(i))
        elif 'sort' in cmd:
            li.sort()
        elif 'pop' in cmd:
            li.pop(-1)
        elif 'reverse' in cmd:
            li.sort(reversed=True)
