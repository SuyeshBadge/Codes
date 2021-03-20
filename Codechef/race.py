# Persistent
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    a.sort()
    b.sort()
    if sum(a[:-1]) == sum(b[:-1]):
        print("Draw")
    elif sum(a[:-1]) < sum(b[:-1]):
        print("Alice")
    elif sum(a[:-1]) > sum(b[:-1]):
        print("Bob")
