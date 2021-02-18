def maxarr(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


def minarr(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min


if __name__ == '__main__':
    arr = list(map(int, input().split(' ')))
    print(minarr(arr))
    print(maxarr(arr))
