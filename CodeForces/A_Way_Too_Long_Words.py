for _ in range(int(input())):
    string = input()
    if len(string) > 10:
        print("{0}{1}{2}".format(string[0], len(string)-2, string[-1]))
    else:
        print(string)
