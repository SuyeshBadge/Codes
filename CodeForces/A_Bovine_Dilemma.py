
def triangleArea(X):
    Y = [1, 0, 0]
    area = 0.0

    j = 2
    for i in range(0, 3):
        area = area + (X[j] + X[i]) * (Y[j] - Y[i])
        j = i

    # Return absolute value
    return abs(area / 2.0)


t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split(' ')))
    arr = []
    for i in x:
        for j in x:
            if j > i:
                X = [0, i, j]
                arr.append(triangleArea(X))

    print(len(set(arr)))
