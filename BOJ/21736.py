from collections import deque


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list("".join(input())))


start = (-1, -1)
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "I":
            start = (i, j)

q = deque()
q.append(start)
matrix[start[0]][start[1]] = -1
cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    cur_x, cur_y = q.popleft()
    for i in range(4):
        nx, ny = cur_x + dx[i], cur_y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == "P":
                cnt += 1

            if matrix[nx][ny] != -1 and matrix[nx][ny] != "X":
                q.append((nx, ny))
                matrix[nx][ny] = -1


print(cnt) if cnt > 0 else print("TT")
