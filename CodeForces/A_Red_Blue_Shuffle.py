from itertools import permutations
t = int(input())
for _ in range(t):
    n = int(input())
    r = input()
    b = input()
    caseR = list(permutations(r))
    # print(caseR)
    caseB = list(permutations(b))
    rc = bc = 0
    for i in range(len(caseB)):
        if int(''.join(caseB[i])) > int(''.join(caseR[i])):
            bc += 1
        elif int(''.join(caseB[i])) < int(''.join(caseR[i])):
            rc += 1
        else:
            continue
    if rc > bc:
        print("RED")
    elif bc > rc:
        print("BLUE")
    else:
        print("EQUAL")
