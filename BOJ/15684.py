from collections import deque

N, M, H = map(int, input().split())
info = []

for _ in range(M):
    a, b = map(int, input().split())
    info.append([a, b])

field = [[0 for _ in range(N)] for _ in range(H)]

for item in info:
    field[item[0] - 1][item[1] - 1] = 1


def check():
    for i in range(N):
        s = i
        for j in range(H):
            if field[j][s] == 1:
                s += 1
            elif s > 0 and field[j][s - 1] == 1:
                s -= 1
        if i != s:
            return False
    return True


ret = 4


def bf(cnt, x, y):
    global ret
    if check():
        ret = min(ret, cnt)
        return
    if cnt == 3 or ret <= cnt:
        return

    for i in range(x, H):
        tmp = 0
        if i == x:
            tmp = y
        for j in range(tmp, N-1):
            if  field[i][j] == 0 and field[i][j + 1] == 0:
                field[i][j] = 1
                bf(cnt + 1, i, j + 2)
                field[i][j] = 0

    return ret


bf(0, 0, 0)
if ret >= 4:
    ret = -1
print(ret)
