from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, dx, dy):
    count = 0
    while field[x + dx][y + dy] != "#" and field[x][y] != "O":
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs(rx, ry, bx, by):
    dq.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    while dq:

        rx, ry, bx, by, paze = dq.popleft()
        if paze > 10:
            break

        for i in range(4):
            mrx, mry, r_cnt = move(rx, ry, dx[i], dy[i])
            mbx, mby, b_cnt = move(bx, by, dx[i], dy[i])
            # print("r: ", mrx, mry, r_cnt)
            # print("b: ", mbx, mby, b_cnt)
            if field[mbx][mby] == "O":
                continue
            if field[mrx][mry] == "O":
                return 1

            if mrx == mbx and mry == mby:
                if r_cnt > b_cnt:
                    mrx -= dx[i]
                    mry -= dy[i]
                else:
                    mbx -= dx[i]
                    mby -= dy[i]

            if not visited[mrx][mry][mbx][mby]:
                visited[mrx][mry][mbx][mby] = True
                dq.append((mrx, mry, mbx, mby, paze + 1))

    return 0


N, M = map(int, input().split())
dq = deque()

field = []
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

for _ in range(N):
    field.append(list(input()))

for i in range(N):
    for j in range(M):
        if field[i][j] == "R":
            rx = i
            ry = j
        if field[i][j] == "B":
            bx = i
            by = j


print(bfs(rx, ry, bx, by))
