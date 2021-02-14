t = int(input())
for i in range(10, 0, -1):
    if t % i == 0:
        print(i)
        break
