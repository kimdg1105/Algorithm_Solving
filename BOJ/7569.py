from collections import deque


m, n, h = map(int, input().split())

arr = []

for z in range(h):
    square = []
    for y in range(n):
        square.append(list(map(int, input().split())))
    arr.append(square)


q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                q.append((k, i, j))


dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

while q:
    z, x, y = q.popleft()

    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:

            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                q.append((nz, nx, ny))


ans = 0
no_ans = False
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 0:
                no_ans = True
            else:
                ans = max(arr[k][i][j], ans)


print(-1) if no_ans else print(ans - 1)
