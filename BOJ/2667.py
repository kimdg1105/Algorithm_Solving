n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, "".join(input().split()))))


def dfs(x, y, count):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    arr[x][y] = 0
    count += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 1:
                count = dfs(nx, ny, count)

    return count


ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            count = dfs(i, j, 0)
            ans.append(count)


ans.sort()

print(len(ans))
for num in ans:
    print(num)
