# CodeBy Suyesh
import math
if __name__ == "__main__":

    for _ in range(int(input())):
        n = int(input())
        w = list(map(int, input().split()))
        l = list(map(int, input().split()))
        index = {}

        for i in range(1, n+1):
            index[i] = w.index(i)
        ans = 0
        for i in range(2, n+1):
            temp1 = index[i]
            temp2 = index[i-1]
            temp = 0
            if temp1 <= temp2:
                temp = (math.ceil((temp2+1-temp1)/l[temp1]))
            ans += temp
            index[i] += temp*(l[temp1])
        print(ans)
