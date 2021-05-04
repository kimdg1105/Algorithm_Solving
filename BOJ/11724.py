from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def bfs(node, adj, visited):
    dq = deque()
    dq.append(node)
    visited[node] = True

    while dq:
        now_node = dq.popleft()
        for i in adj[now_node]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)


N, M = map(int, input().split())
uv =[[] for _ in range(N+1)]
cnt = 0

for i in range(M):
    u, v = map(int, input().split())
    uv[u].append(v)
    uv[v].append(u)


visited = [False for _ in range(len(uv))]

for i in range(1, N + 1):
    if not visited[i]:
        # print("started with", i)
        bfs(i, uv, visited)
        cnt += 1

sys.stdout.write(str(cnt))
