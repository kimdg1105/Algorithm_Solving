from collections import deque
from copy import deepcopy

N,L,R = map(int,input().split())

field = []
visited = [[False for _ in range(N)] for _ in range(N)]
allow = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    field.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# c_num = 1

def check(field, x, y):
    dq = deque()
    flag = False
    dq.append((x,y))
    cnum = 1
    while dq:
        x,y = dq.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if L <= abs(field[x][y] - field[nx][ny]) <= R:
                    allow[x][y] = cnum
                    allow[nx][ny] = cnum
                if not visited[nx][ny]:
                    dq.append((nx,ny))
    return flag

def move(arr):
    union_idx = []
    total = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if allow[i][j] == True:
                union_idx.append((i,j))
                total += field[i][j]
                cnt += 1


    new_arr = deepcopy(field)

    while union_idx:
        i,j = union_idx.pop()
        new_arr[i][j] = total//cnt

    return new_arr


ret = 0
qqq = 0
while qqq < 3:
    visited = [[False for _ in range(N)] for _ in range(N)]
    allow = [[0 for _ in range(N)] for _ in range(N)]

    f = check(field,0,0)
    for n in field:
        print(n)

    print("now arr is ",qqq)
    for a in allow:
        print(a)
    if f:
        field = move(field)
        ret += 1
    else:
        break

    print("new is")

    qqq += 1
print("total",ret)


