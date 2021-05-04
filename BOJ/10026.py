import sys
from collections import deque

input = sys.stdin.readline


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque()
    cur_color = field[x][y]
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        # Q. 왜 23번 라인을 여기 넣으면 메모리 초과일까요?
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if (not visited[nx][ny]) and field[nx][ny] == cur_color:
                    dq.append((nx, ny))
                    visited[nx][ny] = True


N = int(input())
field = []
visited = []
visited2 = []
res1, res2 = 0, 0
for _ in range(N):
    field.append(list(map(str, input())))
    visited.append([False for _ in range(N)])

for i in range(N):
    for j in range(N):
        main_color = field[i][j]
        if not visited[i][j]:
            dfs(i, j)
            res1 += 1

## 적록 친구들
for i in range(N):
    for j in range(N):
        if field[i][j] == "R":
            field[i][j] = "G"

visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        main_color = field[i][j]
        if not visited[i][j]:
            dfs(i, j)
            res2 += 1

print(res1, res2)
