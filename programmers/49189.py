from collections import deque


def solution(n, edge):
    graph = {}
    visited = [False for _ in range(n + 1)]
    visited_dep = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i] = []

    for k, v in edge:
        graph[k].append(v)
        graph[v].append(k)

    start = (1, 0)
    max_dep = 0

    q = deque()
    q.append(start)
    visited[1] = True
    visited_dep[1] = 0

    while q:
        node, cnt = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                visited_dep[next] = cnt + 1
                if max_dep < visited_dep[next]:
                    max_dep = visited_dep[next]
                q.append((next, cnt + 1))

    return visited_dep.count(max_dep)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
