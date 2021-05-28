N = int(input())
graph =[[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = {}

def searchParent(node):
    q = []
    q.append(node)

    while q:
        cur = q.pop()
        for i in graph[cur]:
            if not visited[i]:
                parent[i] = cur
                visited[i] = True
                q.append(i)


searchParent(1)
for i in range(2,N+1):
    print(parent[i])