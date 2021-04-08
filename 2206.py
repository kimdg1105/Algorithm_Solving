from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, z):
    dq = deque()
    dq.append((x, y, 0))

    cost[x][y][0] = 1
    while dq:
        x, y, z = dq.popleft()

        if x == N - 1 and y == M - 1:
            return cost[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # print("ok : ", nx, ny)
                if field[nx][ny] == 0 and cost[nx][ny][z] == -1:
                    cost[nx][ny][z] = cost[x][y][z] + 1
                    dq.append((nx, ny, z))
                elif z == 0 and field[nx][ny] == 1 and cost[nx][ny][1] == -1:
                    cost[nx][ny][z + 1] = cost[x][y][z] + 1
                    dq.append((nx, ny, z + 1))

    return -1


N, M = map(int, input().split())

field = []

for _ in range(N):
    field.append(list(map(int, input())))
cost = [[[-1] * 2 for _ in range(M)] for _ in range(N)]

bfs(0, 0, 0)
ret1 = cost[N - 1][M - 1][0]
ret2 = cost[N - 1][M - 1][1]
ret = 0

if ret1 == -1 and ret2 == -1:
    ret = -1
elif ret1 == -1 and ret2 != -1:
    ret = ret2
else:
    ret = ret1

print(ret)
