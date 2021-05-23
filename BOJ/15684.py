from collections import deque

N,M,H = map(int,input().split())
info = []

for _ in range(M):
    a,b = map(int, input().split())
    info.append([a,b])


field = [[0 for _ in range(N)] for _ in range(H)]


for item in info:
    field[item[0]-1][item[1]-1] = 1

def check():
    flag = True
    for i in range(N):
        node_idx = i-1
        line = 0
        while True:
            if line == H-1:
                break
            if field[line][node_idx] == 1 and 0<=node_idx < N:
                node_idx += 1
                line +=1
                continue
            elif field[line][node_idx-1] == 1 and 1<=node_idx < N:
                node_idx -= 1
                line +=1
                continue
            else:
                line +=1
        if node_idx+1 == i:
            flag = True
        else:
            flag =False

    return flag

for i in field:
    print(i)


print(check())





print(solve(0,0,0))