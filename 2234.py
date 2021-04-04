from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    dq = deque()
    visited[x][y] = True
    dq.append((x, y))
    cnt = 1
    while dq:
        x, y = dq.popleft()
        new_field[x][y] = room
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny]:
                    if i == 0:
                        if field[x][y] & 2:
                            continue
                    elif i == 1:
                        if field[x][y] & 8:
                            continue
                    elif i == 2:
                        if field[x][y] & 1:
                            continue
                    elif i == 3:
                        if field[x][y] & 4:
                            continue
                    visited[nx][ny] = True
                    cnt += 1
                    dq.append((nx, ny))

    return cnt


## main
n, m = map(int, input().split())

field = []
new_field = []
room_size = []
visited = [[False for _ in range(n)] for _ in range(m)]
for _ in range(m):
    field.append(list(map(int, input().split())))
    new_field.append(list([0 for _ in range(n)]))

room, big, rm = 0, 0, 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            room += 1
            room_size.append(bfs(i, j))


for i in range(m):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if new_field[i][j] != new_field[nx][ny]:
                    rm = max(
                        rm,
                        room_size[new_field[i][j] - 1]
                        + room_size[new_field[nx][ny] - 1],
                    )

print(room)
print(max(room_size))
print(rm)
