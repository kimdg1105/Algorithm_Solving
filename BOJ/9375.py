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


    ret = 0
    for i in range(1,len(mydict.keys())+1):
        per = list(combinations(mydict.keys(),i))
        # print("per is",per)
        for item in per:
            if len(item) == 1:
                for e in item:
                    ret += len(mydict[e])

            else:
                tmp = 1
                for e in item:
                    tmp *= len(mydict[e])
                ret += tmp

            # print("now ret is",ret)
    print(ret)


