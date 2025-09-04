from collections import deque


n, m = map(int, input().split())

arr = []
route = [[0 for _ in range(m)] for _ in range(n)]
vistied = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

start_idx = None

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start_idx = (i, j)
            vistied[i][j] = True

q = deque()
q.append(start_idx)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    cur_x, cur_y = q.popleft()
    for i in range(4):
        nx, ny = cur_x + dx[i], cur_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1 and not vistied[nx][ny]:
                route[nx][ny] = route[cur_x][cur_y] + 1
                vistied[nx][ny] = True
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if vistied[i][j] == False and arr[i][j] != 0:
            route[i][j] = -1


for raw in route:
    print(*raw)
