if __name__ == '__main__':
    arr = list(map(int, input().split(' ')))
    k = int(input())
    arr.sort()
    print(arr[k-1])
