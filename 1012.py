from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    visited[x][y] = True
    while dq:
        x,y = dq.popleft()
        if field[x][y] == 0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if field[nx][ny] == 1:
                        dq.append((nx, ny))
                        visited[nx][ny] = True
    return True

T = int(input())
while T:
    M, N, K = map(int, input().split())

    field = []
    field = [list(0 for _ in range(M)) for _ in range(N)]
    visited = [list(False for _ in range(M)) for _ in range(N)]

    # add
    for _ in range(K):
        i,j = map(int,input().split())
        field[j][i] = 1

    bug =0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and field[i][j] != 0:
                if bfs(i,j):
                    bug+=1
    print(bug)

    T -= 1
