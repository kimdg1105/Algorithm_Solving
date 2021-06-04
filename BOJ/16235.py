from collections import deque

N, M, K = map(int,input().split())

field = [[5 for _ in range(N)] for _ in range(N)]

s2d2 = []
for _ in range(N):
    s2d2.append(list(map(int,input().split())))

new_tree = []
dead = []
for _ in range(M):
    x,y,z = map(int,input().split())
    new_tree.append([x,y,z])


def log():
    print("now field:")
    for f in field:
        print(f)

    print('---')
    print("now trees")
    for n in new_tree:
        print(n)


def spring():
    new_tree.sort(key=lambda x: x[2])
    for i in range(len(new_tree)):
        if field[new_tree[i][0]-1][new_tree[i][1]-1] - new_tree[i][2] < 0:
            dead.append(new_tree[i])
            new_tree.pop(i)
        else:
            field[new_tree[i][0]-1][new_tree[i][1]-1] -= new_tree[i][2]
            new_tree[i][2] += 1

def summer():
    for i in range(len(dead)):
        field[dead[i][0]-1][dead[i][1]-1] += int(dead[i][2] / 2)
        dead.pop(i)

def fall():
    global new_tree
    move = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for tree in new_tree:
        if tree[2] % 5 == 0:
            for m in move:
                nx = tree[0] + m[0]
                ny = tree[1] + m[1]

                if 0 <= nx < N and 0 <= ny < N:
                    new_tree.append([nx,ny,1])

def winter():
    for i in range(N):
        for j in range(N):
            field[i][j] += s2d2[i][j]


for _ in range(K):
    spring()
    summer()
    fall()
    winter()

print(len(new_tree))