from collections import deque


m, n = map(int, input().split())
arr = []
for _ in range(n):
    raw = list(map(int, input().split()))
    arr.append(raw)


q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    cur_x, cur_y = q.popleft()

    for i in range(4):
        nx, ny = cur_x + dx[i], cur_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[cur_x][cur_y] + 1
                q.append((nx, ny))


ans = 0
is_false = False
for raw in arr:
    for val in raw:
        if val == 0:
            is_false = True
        else:
            ans = max(ans, val)

print(-1) if is_false else print(ans - 1)
