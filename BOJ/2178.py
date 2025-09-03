from collections import deque


n, m = map(int, input().split())

arr = []
dest_x, dest_y = n - 1, m - 1

for _ in range(n):
    raw = list(map(int, "".join(input().split())))
    arr.append(raw)


q = deque()
start = (0, 0)
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

q.append(start)

while q:
    cur_x, cur_y = q.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = arr[cur_x][cur_y] + 1


print(arr[n - 1][m - 1])
