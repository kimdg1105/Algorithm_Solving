import sys
from math import inf
input = sys.stdin.readline

n = int(input())
m = int(input())

cost = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    cost[a-1][b-1] = min(c, cost[a-1][b-1])


for k in range(n):
    cost[k][k] =0
    for i in range(n):
        for j in range(n):
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

for r in cost:
    for i in range(n):
        if r[i] == inf:
            r[i] = 0
        print(r[i], end=" ")
    print()
