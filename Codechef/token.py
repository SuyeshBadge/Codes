string = '"xyz" abc mnp "asdf dfaa asdf" asd    "fdas asdsdaff"'.split(' ')
i = 0
flag = 0
for i in range(len(string)):
    if len(string[i]) != 0:
        if string[i][0] == '\"' and string[i][-1] == '\"':
            print(string[i])
        elif string[i][0] == '\"':
            flag = 1
            print(string[i], end=' ')

        elif string[i][-1] == '\"' and flag == 1:
            flag = 0
            print(string[i])

        elif flag == 1:
            print(string[i], end=' ')

        else:
            print(string[i])
