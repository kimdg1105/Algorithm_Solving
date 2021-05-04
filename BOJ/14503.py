import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

N, M = map(int,input().split())
cur = list(map(int,input().split()))

field = [list(map(int,input().split())) for _ in range(N)]

cnt =0


def solution(x,y,direction):
    pos = True
    if field[x][y] == 0:
        field[x][y] = 2
    spin_cnt = 0
    while True:
        clean_flag = False
        for i in range(4):
            nx = x + dx[(direction + 3 - i) % 4]
            ny = y + dy[(direction + 3 - i) % 4]
            if field[nx][ny] == 0:
                x, y = nx, ny
                direction = (direction + 3 - i) % 4
                field[x][y] = 2
                clean_flag = True
                break

        if field[nx][ny] == 0:
            x,y = nx,ny
            field[x][y] = 2
            clean_flag = True

        if clean_flag:
            spin_cnt+=1
            continue

        nx = x + dx[(direction + 2) % 4]
        ny = y + dy[(direction + 2) % 4]

        if field[nx][ny] == 1:
            pos = False
        else:
            x, y = nx, ny

        if not pos:
            break

        # elif field[nx][ny] == 1 or field[nx][ny] == 2:
        #     print("wall, with spin:",spin_cnt)
        #     spin_cnt += 1
        #     continue


solution(cur[0],cur[1],cur[2])

# for i in field:
#     print(i)

for i in field:
    for j in i:
        if j == 2:
            cnt +=1
print(cnt)