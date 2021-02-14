def isPrime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False


for _ in range(int(input())):
    ln = int(input())
    ar = list(map(int, input().split(' ')))
    ans = []
    for n in ar:
        c = 0
        i = n
        while i <= n and i > 1:
            if n == 0:
                break
            elif n == 1:
                c += 1

            elif isPrime(i):
                n -= i
                c += 1
                i = n
            else:
                i -= 1
        else:
            if n == 1:
                ans.append(c+1)
            else:
                ans.append(c)
    print(sum(ans))
