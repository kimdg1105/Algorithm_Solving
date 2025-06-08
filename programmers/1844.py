def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * n for _ in range(m)]

    start = [0, 0]
    ans = dfs(start, visited, n, m, maps, 0)
    print(ans)
    return answer


def dfs(xy, visited, n, m, maps, cnt):
    visited[xy[0]][xy[1]] = True

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    for i in range(4):
        nx, ny = xy[0] + dx[i], xy[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny, n, m, maps, cnt + 1)


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
