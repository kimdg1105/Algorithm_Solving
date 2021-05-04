N, M = map(int,input().split())

l1 = []
l2 = []
for _ in range(N):
    l1.append(input())
for _ in range(M):
    l2.append(input())

l1 = set(l1)
l2 = set(l2)

ret = []
cnt = 0
for name in l2:
    if name in l1:
        cnt +=1
        ret.append(name)

print(cnt)
ret.sort()
for i in range(len(ret)):
    print(ret[i])
