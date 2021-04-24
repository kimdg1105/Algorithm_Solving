import sys
import bisect


input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))

set_l = list(set(l))
set_l.sort()



for i in range(N):
    new_idx = bisect.bisect(set_l, l[i])
    l[i] = new_idx-1

for i in range(N):
    sys.stdout.write(str(l[i]) + ' ')
