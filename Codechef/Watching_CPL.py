for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    h = list(map(int, input().split(' ')))
    temp = h.copy()
    temp.sort(reverse=True)
    m = []
    t = []
    if sum(temp) < 2*k:
        print(-1)
    elif sum(temp) == 2*k:
        print(len(temp))
    elif sum(temp) > 2*k:
        a = b = True
        i = 0
        while a or b:
            if a == True:
                if i < len(temp)-1 and sum(m)+temp[i+1] >= k:
                    m.append(temp[i+1])
                    temp.pop(i+1)
                elif sum(m) <= k:
                    m.append(temp[i])
                    i += 1
                if sum(m) >= k:
                    a = False
            if b == True:
                if i < len(temp)-1 and sum(t)+temp[i+1] >= k:
                    t.append(temp[i+1])
                    temp.pop(i+1)
                elif sum(t) <= k:
                    t.append(temp[i])
                    i += 1
                if sum(t) >= k:
                    b = False

        print(len(m)+len(t))
