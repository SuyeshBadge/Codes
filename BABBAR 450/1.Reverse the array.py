def reverse(arr):
    i = 0
    n = len(arr)-1
    while i < n:
        arr[i], arr[n] = arr[n], arr[i]
        i += 1
        n -= 1
    return(list(map(str, arr)))


if __name__ == "__main__":
    # arr = list(map(int, input().split(' ')))
    arr = [1, 5, 7, 6, 9, 3, 4]
    print(" ".join(reverse(arr)))
