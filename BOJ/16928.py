from collections import deque


ladder = {}
sneake = {}
arr = [0 for _ in range(101)]
visited = [False for _ in range(101)]
dice = [1, 2, 3, 4, 5, 6]
start, end = 1, 100

n, m = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    sneake[u] = v


q = deque()
q.append(start)
visited[start] = True

while q:
    cur = q.popleft()
    if cur == end:
        print(arr[cur])
        break

    for dot in dice:
        next = cur + dot
        if next in ladder.keys():
            next = ladder[next]
        if next in sneake.keys():
            next = sneake[next]
        if 1 <= next <= 100 and not visited[next]:
            q.append(next)
            visited[next] = True
            arr[next] = arr[cur] + 1
