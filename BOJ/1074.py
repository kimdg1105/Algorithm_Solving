import sys

sys.setrecursionlimit(100000)
N, r, c = map(int, input().split())
cnt = 0

def divide(s, nx, ny):
    global cnt
    if nx == r and ny == c:
        print(cnt)
        exit(0)
    elif s == 1:
        cnt += 1
        return
    if not (nx <= r < nx + s) and not (ny <= c < ny + s):
        cnt += s ** 2
        return
    divide(s // 2, nx, ny)
    divide(s // 2, nx, ny + s // 2)
    divide(s // 2, nx + s // 2, ny)
    divide(s // 2, nx + s // 2, ny + s // 2)


divide(2 ** N, 0, 0)
