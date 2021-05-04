import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nl = list(map(int,input().split()))

s,e = 0,0
flag = 0
ret = sys.maxsize
sum = 0
while s != N:
    if sum < M and e < N:
        sum += nl[e]
        e += 1
    else:
        sum -= nl[s]
        s += 1
    if sum >= M:
        ret = min(ret,e-s)
        flag = 1


    #print("now sum,s,e", sum, s, e, ret)

if flag == 0:
    print(0)
else:
    print(ret)
