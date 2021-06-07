from collections import deque

N = int(input())
field = []

for _ in range(N):
    field.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if field[i][j] == 9:
            stx,sty = i,j

def show():
    print("HI")
    for f in field:
        print(f)

def bfs(x,y,size):
    cnt = 1
    ret = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    dq = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]

    dq.append((x,y,size,cnt))
    visited[x][y] = True

    while dq:
        x,y,size,cnt = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:


                if field[nx][ny] > size:
                    continue

                if field[nx][ny] != 0:
                    if field[nx][ny] < size:
                        ret.append((nx,ny,cnt))

                visited[nx][ny] = True
                dq.append((nx,ny,size,cnt+1))

    return ret

size = 2
time = 0
# show()
eat_cnt = 0
while True:

    # print("mysize",size,"Eat",eat_cnt,'time',time, 'x',stx,'y', sty)
    # show()
    can_eat = bfs(stx, sty, size)
    # print(can_eat)

    if len(can_eat) >= 1:
        if len(can_eat) > 1:
            can_eat.sort(key = lambda x:(x[2],x[0], x[1]))
        field[stx][sty] = 0
        time += can_eat[0][2]
        stx,sty = can_eat[0][0], can_eat[0][1]

        if field[stx][sty] < size:
            eat_cnt += 1
            if eat_cnt == size:
                size += 1
                eat_cnt = 0

        field[stx][sty] = 9

    if len(can_eat) == 0:
        print(time)
        break




