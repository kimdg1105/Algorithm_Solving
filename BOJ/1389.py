from collections import deque


n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = []
ret = 5001
ret_idx = 101

for i in range(1, n + 1):
    visited = [-1 for _ in range(n + 1)]
    q = deque()

    q.append(i)
    visited[i] = 0

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur] + 1

    kevin = sum(visited)
    ans.append(kevin)


print(ans.index(min(ans)) + 1)
