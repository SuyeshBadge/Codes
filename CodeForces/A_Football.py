s = input()

c = 1
for i in range(1, len(s)):
    if c < 7:
        if s[i] == s[i-1]:
            c += 1
        else:
            c = 1
    else:
        break
if c >= 7:
    print("YES")
else:
    print("NO")
