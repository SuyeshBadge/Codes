t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    encode = {'a': '0000',
              'b': '0001',
              'c': '0010',
              'd': '0011',
              'e': '0100',
              'f': '0101',
              'g': '0110',
              'h': '0111',
              'i': '1000',
              'j': '1001',
              'k': '1010',
              'l': '1011',
              'm': '1100',
              'n': '1101',
              'o': '1110',
              'p': '1111'}
    str1 = []
    for i in range(0, len(s), 4):
        str1.append(s[i:i+4])
    for i in str1:
        for k, v in encode.items():
            if i == v:
                print(k, end='')
    print()
