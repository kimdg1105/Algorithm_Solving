import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
dq = deque()
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

cnt = 0

def dfs():
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while dq:
        x, y, day = dq.popleft()
        day += 1
        # print("xy = ", x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == -1:
                    continue
                if field[nx][ny] == 0:
                    field[nx][ny] = 1
                    cnt += 1
                    dq.append((nx, ny, day))
    return day


for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            dq.append((i, j,0))

ret = dfs() - 1

for i in field:
    for j in i:
        if j == 0:
           ret = -1

print(ret)