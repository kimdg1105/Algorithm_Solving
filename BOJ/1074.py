from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, num):
    dq = deque()
    dq.append((x, y, num))
    field[x][y] = num

    while dq:
        x, y, num = dq.popleft()
        if num < 4:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < pow(2, N) and 0 <= ny < pow(2, N):
                    if num == 0:
                        nx = x
                        ny = y + 1
                    elif num == 1:
                        nx = x + 1
                        ny = y - 1
                    elif num == 2:
                        nx = x
                        ny = y + 1
                    num += 1
                    field[nx][ny] = num
                    dq.append((nx, ny, num))
                    visited[nx][ny] = True


N, r, c = map(int, input().split())
field = [list(0 for _ in range(pow(2, N))) for _ in range(pow(2, N))]
visited = [list(False for _ in range(pow(2, N))) for _ in range(pow(2, N))]

idx = 0

for i in range(pow(2, N)):
    for j in range(pow(2, N)):
        if not visited[i][j]:
            bfs(i, j, 0)

for i in range(pow(2, N)):
    print(field[i])
