import sys
input = sys.stdin.readline

N = int(input())
liq = list(map(int,input().split()))

ret = sys.maxsize
start, end = 0, N-1
ans = []

liq.sort()
while start != end :

    cur = liq[start] + liq[end]
    #print("now: ", start, end, cur)
    if cur == 0:
        ans.append([liq[start],liq[end]])
        break
    if abs(cur) <= abs(ret):
       # print("  new cur", liq[start],liq[end], cur)
        ret = cur
        ans.append([liq[start],liq[end]])
    if cur > 0:
        end -= 1
    elif cur < 0:
        start += 1


#print(ans)
print(ans[-1][0], ans[-1][1])