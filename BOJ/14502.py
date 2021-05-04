import sys
from collections import  deque

input = sys.stdin.readline

N, M = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
field = []

for _ in range(N):
    field.append(list(map(int,input().split())))

white_space = []
for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
           white_space.append([i,j])


def dfs(wall):
    ret = 0
    dq = deque()
    copy_field = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy_field[i][j] = field[i][j]
    for i in wall:
        copy_field[i[0]][i[1]] = 1

    for i in range(N):
        for j in range(M):
            if copy_field[i][j] == 2:
                dq.append((i,j))

    while dq:
        x, y = dq.popleft()
        if copy_field[x][y] == 2:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if copy_field[nx][ny] == 1:
                        continue
                    if copy_field[nx][ny] == 0:
                        copy_field[nx][ny] = 2
                        dq.append((nx,ny))

    for i in range(N):
        for j in range(M):
            if copy_field[i][j] == 0:
                ret += 1

    return ret




max_ret = 0

for i in range(len(white_space)):
    for j in range(i+1,len(white_space)):
        for k in range(j+1,len(white_space)):
            wall = [white_space[i],white_space[j],white_space[k]]
            ret = dfs(wall)
            if ret > max_ret:
                max_ret = ret
                # for q in field:
                #     print(q)

print(max_ret)