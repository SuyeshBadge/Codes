for _ in range(int(input())):
    a, b, c, r = map(int, input().split(' '))
    cr = list(range(a, b))
    if (a <= 0 and b >= 0) or (a >= 0 and b <= 0):
        if c < b and c > a:
            print(abs(a)+abs(b)-r)
        elif c == a or c == b:
            print((abs(a)+abs(b))-(r//2))
        else:
            if c+(r//2) in cr:
                print(abs(a)+abs(b)+(c+r//2))
            else:
                print(abs(a)+abs(b))

    else:
        if c < b and c > a:
            print(abs(abs(a)-abs(b))-r)
        elif c == a or c == b:
            print(abs((abs(a)-abs(b)))-(r//2))
        else:
            if c+r in cr:
                print(abs(abs(a)-abs(b))+(c+r))
            else:
                print(abs(a)-abs(b))
