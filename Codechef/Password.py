import string


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


for _ in range(int(input())):
    p = input()
    flag = False
    if len(p) >= 10:
        ch = p[1:-1:1]
        sym = ['@', '#', '%', '&', '?']
        lw = list(string.ascii_letters)
        num = list(range(10))
        if hasNumbers(ch):
            for i in ch:

                if i in sym or i in lw or i in num:
                    flag = True
                else:
                    flag = False
        else:
            flag = False
        if flag == True:
            print("YES")
        else:
            print("NO")
    else:
        print('NO')
