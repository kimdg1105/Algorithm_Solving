from _collections import deque
import sys

input = sys.stdin.readline


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque()
    dq.append((x, y))
    visited[x][y] = 1
    o_cnt, v_cnt = 0, 0
    while dq:
        x, y = dq.popleft()
        if graph[x][y] == "o":
            o_cnt += 1
        if graph[x][y] == "v":
            v_cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < R
                and 0 <= ny < C
                and visited[nx][ny] != 1
                and graph[nx][ny] != "#"
            ):
                dq.append((nx, ny))
                visited[nx][ny] = 1

    if o_cnt > v_cnt:
        v_cnt = 0
    else:
        o_cnt = 0
    return o_cnt, v_cnt


R, C = map(int, input().split())

graph = []
visited = []
for _ in range(R):
    graph.append(list(map(str, input())))
    visited.append([0 for _ in range(C)])

r_o_cnt, r_v_cnt = 0, 0

for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and (graph[i][j] == "v" or graph[i][j] == "o"):
            o, v = dfs(i, j)
            r_o_cnt += o
            r_v_cnt += v

print(r_o_cnt, r_v_cnt)
