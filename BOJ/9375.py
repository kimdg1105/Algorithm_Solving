import sys
from itertools import combinations

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    wear = {}
    l = []
    for _ in range(n):
        a,b = map(str,input().split())
        l.append((a,b))

    mydict = {}
    for i in range(len(l)):
        if l[i][1] not in mydict:
            mydict[l[i][1]] = []

    for i in range(len(l)):
        mydict[l[i][1]].append(l[i][0])

    # print(mydict)


    ret = 1
    for key in mydict:
        ret *= len(mydict[key]) + 1
    ret -= 1
            # print("now ret is",ret)
    print(ret)


