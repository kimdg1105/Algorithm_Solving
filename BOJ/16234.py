from collections import deque
from copy import deepcopy

N, L, R = map(int,input().split())

field = []

for _ in range(N):
    field.append(list(map(int,input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    dq = deque()
    union = []
    dq.append((x,y))
    union.append((x,y))
    visited[x][y] = True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(field[nx][ny] - field[x][y]) <= R:
                    union.append((nx,ny))
                    visited[nx][ny] = True
                    dq.append((nx, ny))
    return union

ret = 0

while True:
    flag = False
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                ul = bfs(i,j)
                if len(ul) > 1:
                    flag = True
                    people = 0
                    for p in ul:
                        people += field[p[0]][p[1]]
                    people = people // len(ul)
                    for p in ul:
                        field[p[0]][p[1]] = people

    if flag == False:
        break
    ret += 1


print(ret)

