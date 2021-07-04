from collections import deque
import sys

N = int(input())

field = []
height = []

for _ in range(N):
    field.append(input())
for _ in range(N):
    height.append(list(map(int,input().split())))

for f in field:
    print(f)
print("----")
for h in height:
    print(h)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

minh = sys.maxsize
maxh = 0

for i in range(N):
    for j in range(N):
        if field[i][j] == 'P':
            x,y = i,j

def bfs(x,y):
    dq = deque()
    dq.append((x,y))

    while dq:
        x,y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                ~~~
