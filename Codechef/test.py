def minlex(s1):
    s = s1+s1
    of = 0
    ans = 0
    for i in range(1, len(s)):
        if s[i] < s[ans]:
            ans = i
            of = 0
        elif s[i] == s[ans+of]:
            of += 1
        elif s[i] < s[ans+of]:
            ans = i-of
            of = 0
            i = ans
        else:
            of = 0
    print(s[ans:ans+len(s1)])


minlex('abaacbac')
