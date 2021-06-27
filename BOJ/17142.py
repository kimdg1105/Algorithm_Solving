from collections import deque
from itertools import combinations
from copy import deepcopy
import sys

n, m = map(int, input().split())
field = []
room = [[-1 for _ in range(n)] for _ in range(n)]
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    field.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if field[i][j] == 1:
            room[i][j] = '-'
        if field[i][j] == 2:
            room[i][j] = '*'
            virus.append((i, j, 0))

comb_v = list(combinations(virus, m))


def bfs(stage, vi):
    visited = [[False for _ in range(n)] for _ in range(n)]
    dq = deque()
    for v in vi:
        dq.append(v)
    while dq:
        x, y, time = dq.popleft()
        visited[x][y] = True

        if stage[x][y] != '-':
            # if room[x][y] == "*":
            #     continue
            # if room[x][y] <= time:
            #     continue

            if type(stage[x][y]) == int and stage[x][y] < time and not stage[x][y] == -1:
                continue
            else:
                stage[x][y] = time

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if stage[nx][ny] == '-':
                    continue
                if stage[nx][ny] == -1:
                    dq.append((nx, ny, time + 1))

    # print(*stage, sep="\n")
    # print("____")
    return stage


def maxtime(arr):
    mt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                return False

            if type(arr[i][j]) == int and arr[i][j] >= mt:
                mt = arr[i][j]
    # print("mt is",mt)
    if mt == 0:
        print(0)
        exit()
    return mt


min_ret = sys.maxsize
temp = sys.maxsize
for v in comb_v:
    stage = deepcopy(room)
    case = bfs(stage, v)
    mc = maxtime(case)
    if mc != False:
        temp = mc
    min_ret = min(min_ret, temp)
    # print("G",min_ret)





# def ok(arr):
#     flag =True
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] != '*' or arr[i][j] != '-' or arr[i][j] != 0:
#                 return False
#     return flag

if min_ret == sys.maxsize:
    if mc == False:
        print(-1)
else:
    print(min_ret)

# #
# print(*field, sep='\n')
#
# print(*room, sep='\n')
#
# print("vir",comb_v)
