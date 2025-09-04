from heapq import heappop, heappush
import sys

input = sys.stdin.readline


n = int(input())

total_pq = []

for _ in range(n):
    num = int(input())

    if num != 0:
        heappush(total_pq, (abs(num), num))

    else:
        if len(total_pq) == 0:
            print(0)

        else:
            ret = heappop(total_pq)
            print(ret[1])
