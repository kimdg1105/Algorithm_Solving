from collections import  deque

N = int(input())
cmd = []

field = [[0 for _ in range(101)] for _ in range(101)]

dx = [-1,1,0,0] # 북 남 서 동
dy = [0,0,-1,1]

for _ in range(N):
    cmd.append(list(map(int,input().split())))

for c in cmd:
    move = deque()
    move.append(c[2])
    for _ in range(c[3]):
        tmp = list(reversed(move))
        for t in range(len(tmp)):
            tmp[t] +=1
            if tmp[t] == 4:
                tmp[t] = 0
            move.append(tmp[t])


    sx,sy = c[1], c[0]
    field[sx][sy] = 1

    while move:
        direct = move.popleft()
        if direct == 0:
            nx = sx + dx[3]
            ny = sy + dy[3]
        elif direct == 1:
            nx = sx + dx[0]
            ny = sy + dy[0]
        elif direct == 2:
            nx = sx + dx[2]
            ny = sy + dy[2]
        elif direct == 3:
            nx = sx + dx[1]
            ny = sy + dy[1]

        field[nx][ny] = 1
        sx, sy = nx, ny



#
# for f in field:
#     print(f)

ret = 0
for i in range(100):
    for j in range(100):
        if field[i][j] == 1:
            if field[i+1][j] == 1 and field[i][j+1] == 1 and field[i+1][j+1] == 1:
                ret += 1

print(ret)