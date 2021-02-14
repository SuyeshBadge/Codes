# CodeBy Suyesh
def isSame(arr):
    return arr.count(arr[0]) == len(arr)


if __name__ == "__main__":

    for _ in range(int(input())):
        num = int(input())
        a = list(map(int, input().split(' ')))
        if isSame(a):
            print(0)
        else:
            ans = []
            ar = list(set(a))
            x = max(ar)
            z = min(ar)

            for y in ar:
                ans.append(abs(x-y)+abs(y-z)+abs(z-x))
            print(max(ans))
