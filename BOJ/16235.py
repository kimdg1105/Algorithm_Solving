import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

field = [[5 for _ in range(N)] for _ in range(N)]

s2d2 = []

for _ in range(N):
    s2d2.append(list(map(int, input().split())))

tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,z = map(int, input().split())
    tree[x-1][y-1].append(z)

def log():
    print("now field:")
    for f in field:
        print(f)

    print('---')
    print("now trees")
    for n in tree:
        print(n)


def spring():
    dead = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                for k in range(len(tree[i][j])):
                    if tree[i][j][k] != -1:
                        if field[i][j] - tree[i][j][k] < 0:
                            dead[i][j].append(k)
                        else:
                            field[i][j] -= tree[i][j][k]
                            tree[i][j][k] += 1
                for idx in range(len(dead[i][j])-1,-1,-1):
                    temp = tree[i][j][dead[i][j][idx]]
                    del tree[i][j][dead[i][j][idx]]
                    field[i][j] += int(temp / 2)

    # print("Spring",tree)


def fall():
    temp = []
    move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for k in range(len(tree[i][j])):
                    if tree[i][j][k] % 5 == 0:
                        for m in move:
                            nx = i + m[0]
                            ny = j + m[1]
                            if 0 <= nx < N and 0 <= ny < N:
                                tree[nx][ny].append(1)

    # print("Fall",tree)


def winter():
    for i in range(N):
        for j in range(N):
            field[i][j] += s2d2[i][j]



for _ in range(K):
    # log()
    spring()
    fall()
    winter()

ret = 0
for i in range(N):
    for j in range(N):
        ret += len(tree[i][j])


print(ret)
